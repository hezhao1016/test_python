# 网易云音乐批量下载歌曲图片

import requests
import urllib.request
import os

path = 'F:/网易云音乐'
flag = os.path.exists(path)
if not flag:
    os.mkdir(path)

# GET被网易屏蔽，使用POST访问
r = requests.post('http://music.163.com/api/playlist/detail',
                  data={'id': '393565693'},
                  headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"})

arr = r.json()['result']['tracks']
print(arr)

for i, music in enumerate(arr):
    name = str(i+1) + '-' + music['name'] + '.jpg'
    link = music['album']['picUrl']

    # 1、直接将远程数据下载到本地
    urllib.request.urlretrieve(link, os.path.join(path, name))

    # 2、读取字节，然后自行写入
    # data = requests.get(link).content
    # with open(os.path.join('F:/网易云音乐1', name),'wb') as targetFile:
    #     targetFile.write(data)

    print(name + ' 歌曲图片下载完成')