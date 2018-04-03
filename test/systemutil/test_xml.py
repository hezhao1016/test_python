# XML

# DOM vs SAX
# 操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
# 正常情况下，优先考虑SAX，因为DOM实在太占内存。
# 在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。

# 举个例子，当SAX解析器读到一个节点时
# <a href="/">python</a>

# 会产生3个事件：

# start_element事件，在读取<a href="/">时；
# char_data事件，在读取python时；
# end_element事件，在读取</a>时。

# 用代码实验一下 SAX

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parse = ParserCreate()
parse.StartElementHandler = handler.start_element
parse.EndElementHandler = handler.end_element
parse.CharacterDataHandler = handler.char_data
parse.Parse(xml)

# 需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并。



# SAX读取xml文件
'''
ContentHandler类方法介绍
    characters(content)方法
        调用时机：
        从行开始，遇到标签之前，存在字符，content的值为这些字符串。
        从一个标签，遇到下一个标签之前， 存在字符，content的值为这些字符串。
        从一个标签，遇到行结束符之前，存在字符，content的值为这些字符串。
        标签可以是开始标签，也可以是结束标签。
    startDocument()方法
        文档启动的时候调用。
    endDocument()方法
        解析器到达文档结尾时调用。
    startElement(name, attrs)方法
        遇到XML开始标签时调用，name是标签的名字，attrs是标签的属性值字典。
    endElement(name)方法
        遇到XML结束标签时调用。
    
    make_parser()方法
    以下方法创建一个新的解析器对象并返回。
    xml.sax.make_parser( [parser_list] )
    参数说明:
        parser_list - 可选参数，解析器列表
    
    parser()方法
    以下方法创建一个 SAX 解析器并解析xml文档：
    xml.sax.parse( xmlfile, contenthandler[, errorhandler])
    参数说明:
        xmlfile - xml文件名
        contenthandler - 必须是一个ContentHandler的对象
        errorhandler - 如果指定该参数，errorhandler必须是一个SAX ErrorHandler对象
    
    parseString()方法
    parseString方法创建一个XML解析器并解析xml字符串：
    xml.sax.parseString(xmlstring, contenthandler[, errorhandler])
    参数说明:
        xmlstring - xml字符串
        contenthandler - 必须是一个ContentHandler的对象
        errorhandler - 如果指定该参数，errorhandler必须是一个SAX ErrorHandler对象
'''
print('======================SAX读取xml文件=====================')
import xml.sax

class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # 元素开始调用
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("*****Movie*****")
            title = attributes["title"]
            print("Title:", title)

    # 元素结束调用
    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "rating":
            print("Rating:", self.rating)
        elif self.CurrentData == "stars":
            print("Stars:", self.stars)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""

    # 读取字符时调用
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


if (__name__ == "__main__"):
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("../../files/movies.xml")




# DOM读取xml文件
print('====================DOM读取xml文件==================')
from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("../../files/movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print ("Root element : %s" % collection.getAttribute("shelf"))

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
   print ("*****Movie*****")
   if movie.hasAttribute("title"):
      print ("Title: %s" % movie.getAttribute("title"))

   type = movie.getElementsByTagName('type')[0]
   print ("Type: %s" % type.childNodes[0].data)
   format = movie.getElementsByTagName('format')[0]
   print ("Format: %s" % format.childNodes[0].data)
   rating = movie.getElementsByTagName('rating')[0]
   print ("Rating: %s" % rating.childNodes[0].data)
   description = movie.getElementsByTagName('description')[0]
   print ("Description: %s" % description.childNodes[0].data)




print('=================生成XML=================')
# 除了解析XML外，如何生成XML呢？99%的情况下需要生成的XML结构都是非常简单的，因此，最简单也是最有效的生成XML的方法是拼接字符串
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(r'some & data')
L.append(r'</root>')
xml = ''.join(L)
print(xml)


# 小结
# 解析XML时，注意找出自己感兴趣的节点，响应事件时，把节点数据保存起来。解析完毕后，就可以处理数据。




print('====================================')
# 练习 | 请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：
# https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml
# 参数woeid是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。

from xml.parsers.expat import ParserCreate
from urllib import request
from datetime import datetime

class CitySaxHandler(object):
    def __init__(self):
        self.data = {}

    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
        if name == 'yweather:location':
            self.data['city'] = attrs['city']
        elif name == 'yweather:forecast':
            if 'forecast' not in self.data:
                self.data['forecast'] = []

            # 日期格式化
            cday = datetime.strptime(attrs['date'], '%d %b %Y')
            datestr = cday.strftime('%Y-%m-%d')

            weather = {
                'date': datestr,
                'high': attrs['high'],
                'low': attrs['low']
            }
            self.data['forecast'].append(weather)

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

def parseXml(xml_str):
    print(xml_str)

    handler = CitySaxHandler()
    parse = ParserCreate()
    parse.StartElementHandler = handler.start_element
    parse.EndElementHandler = handler.end_element
    parse.CharacterDataHandler = handler.char_data
    parse.Parse(xml_str)

    return handler.data

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
print('Result: ', result)
assert result['city'] == 'Beijing'
print('ok!')

