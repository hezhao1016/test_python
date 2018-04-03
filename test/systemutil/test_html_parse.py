# HTMLParser

# 如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。
# 假设第一步已经完成了，第二步应该如何解析HTML呢？
# HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
# 好在Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码


from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        # 打印属性
        attr_str = ''
        for i, a in enumerate(attrs):
            if i == 0:
                attr_str = ' '
            attr_str += '%s=\"%s\"' % (a[0], a[1])
        print('<%s%s>' % (tag, attr_str))

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        # 打印属性
        attr_str = ''
        for i, a in enumerate(attrs):
            if i == 0:
                attr_str = ' '
            attr_str += '%s=\"%s\"' % (a[0], a[1])
        print('<%s%s/>' % (tag, attr_str))

    def handle_data(self, data):
        if data and len(data.strip()) > 0:
            print(data.strip())

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some [&#1234;]<a href=\"#\">html</a> HTML&nbsp;tutorial...<br class="brb" />END</p>
</body></html>''')


# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
# 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来


# 小结
# 利用HTMLParser，可以把网页中的文本、图像等解析出来。



# 练习 | 找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。

from html.parser import HTMLParser
from urllib import request
from datetime import datetime

class MyHTMLParser(HTMLParser):

    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.__currentTag = ''
        self.__currentData = ''
        self.__currentTime = ''
        self.data = []

    def handle_starttag(self, tag, attrs):
        if tag == 'ul':
            for a in attrs:
                if a[0] == 'class' and a[1] == 'list-recent-events menu':
                    self.__currentTag = 'ul'
                    break

        if self.__currentTag == 'ul' and tag == 'h3':
            for a in attrs:
                if a[0] == 'class' and a[1] == 'event-title':
                    self.__currentTag = 'h3'
                    break

        if self.__currentTag == 'h3' and tag == 'a':
            self.__currentData = 'title'

        if self.__currentTag == 'ul' and tag == 'time':
            self.__currentTag = 'time'
            self.__currentData = 'time'

        if self.__currentTag == 'time' and tag == 'span':
            for a in attrs:
                if a[0] == 'class' and a[1] == 'say-no-more':
                    self.__currentData = 'year'
                    break

        if self.__currentTag == 'ul' and tag == 'span':
            for a in attrs:
                if a[0] == 'class' and a[1] == 'event-location':
                    self.__currentData = 'location'
                    break

    def handle_endtag(self, tag):
        if self.__currentTag == 'ul' and tag == 'ul':
            self.__currentTag = ''

        if (self.__currentTag == 'h3' and tag == 'h3') or \
                (self.__currentTag == 'time' and tag == 'time'):
            self.__currentTag = 'ul'

    def handle_data(self, data):
        data = data.strip()
        if self.__currentTag != '' and self.__currentData != '':
            if self.__currentData == 'title':
                self.data.append({'标题': data, '时间': '', '地点': ''})
            if self.__currentData == 'time':
                self.__currentTime = data
            if self.__currentData == 'year':
                f = '%d %B%Y'
                if self.__currentTime.find(". – ") != -1:
                    f = '%d %b%Y'
                    self.__currentTime = self.__currentTime.replace('.', '')
                index = self.__currentTime.find(' – ')
                startTime = self.__currentTime[:index] + data
                endTime = self.__currentTime[index + len(' – '):] + data
                startTime_date = datetime.strptime(startTime, f)
                endTime_date = datetime.strptime(endTime, f)
                self.data[-1]['时间'] = startTime_date.strftime('%Y-%m-%d') + ' 至 ' + endTime_date.strftime('%Y-%m-%d')
            if self.__currentData == 'location':
                self.data[-1]['地点'] = data
            self.__currentData = ''

parser = MyHTMLParser()
with request.urlopen('https://www.python.org/events/python-events/') as f:
    html = f.read().decode('utf-8')
parser.feed(html)

if parser.data:
    for row in parser.data:
        print('==============================')
        for key, value in row.items():
            print('%s:%s' % (key, value))

