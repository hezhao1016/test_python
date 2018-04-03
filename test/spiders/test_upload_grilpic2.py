# 下载美女图片

from bs4 import BeautifulSoup
import requests
import os
from datetime import datetime
from functools import reduce
from test.thread.threadpool.test_my_threadpool import ThreadPool

# 网站
urls = 'http://095j.com/girl.htm'

# url前缀
front_urls = 'http://095j.com'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
}

base_path = 'G:/美女图片/095j.com/'

# 打印日志
def log(*args):
    now = datetime.now()
    datestr = now.strftime('%Y-%m-%d %H:%M:%S')

    out = ''
    if isinstance(args, tuple):
        out = reduce(lambda x, y: '%s %s' % (x, y), args)
    else:
        out = args

    print(datestr, ':', out)

# 创建文件夹
def mkdir(name, path):
    path = path.strip()
    file_path = os.path.join(os.path.join(base_path, name), path)
    isExists = os.path.exists(file_path)
    if not isExists:
        log(u'新建 ', path, u' 文件夹...')
        os.makedirs(file_path)
        return True
    else:
        log(u'名字叫做', path, u'的文件夹已经存在了！')
        return False

# 过滤文件名特殊符号
def filter_dir_name(dir_name):
    strs = ['\\', '/', ':', '*', '?', '\"', '<', '>', '|']

    for s in strs:
        dir_name = str(dir_name).replace(s, '')

    return dir_name

# 获取文章列表页
def get_html(name, url, page_index=1):
    try:
        if page_index and page_index > 1:
            url += '/%s.htm' % page_index
        html = requests.get(url).content
        s = BeautifulSoup(html, 'lxml')
        picList = s.select('div.tu_list li a')
        page_size = s.find('div', class_='pagination').text
        page_size = int(page_size[page_size.rfind('/') + 1: page_size.rfind('页')])
        get_pic(name, url, page_index, page_size, picList)
    except Exception as e:
        log('出现异常', e)

# 获取图片
def get_pic(name, url, page_index, page_size, picList):
    log('\n============正在下载[%s]第%s页图片,共%s页============' % (name, page_index, page_size))
    for pic in picList:
        img_dir_name = pic['title']
        img_dir_name = filter_dir_name(img_dir_name)
        mkdir(name, img_dir_name)
        log(img_dir_name, pic['href'])

        img_html = requests.get(front_urls + pic['href']).content
        s = BeautifulSoup(img_html, 'lxml')
        imgs = s.select('div.pics img')

        i = 0
        for img in imgs:
            i += 1
            ext = img['src'][img['src'].rfind('.'):]

            img_source = requests.get(img['src'], headers=headers)
            file_path = os.path.join(os.path.join(os.path.join(base_path, name), img_dir_name), str(i) + ext)
            f = open(file_path, 'wb')
            f.write(img_source.content)
            f.close()

            log('图片[%s]下载完成' % img['src'])

    if(page_index < page_size):
        get_html(name, url, page_index + 1)


print('开始下载美女图片...\n================================================')
pool = ThreadPool(52)
page_index = 1

# 线程池添加任务
gril_html = requests.get(urls).content
s = BeautifulSoup(gril_html, 'lxml')

# 图片区
gril_list = s.select('div.k_head-2a')[2].select('li a')
for gril in gril_list:
    name = gril.text
    img_page_url = front_urls + gril['href']
    pool.callInThread(get_html, name, img_page_url, page_index)

# 套图区
gril_list = s.select('div.tu_list li a')
for gril in gril_list:
    name = gril['title']
    img_page_url = front_urls + gril['href']
    pool.callInThread(get_html, name, img_page_url, page_index)

pool.start()
pool.stop()
