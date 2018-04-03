# https://cuiqingcai.com/2621.html
# https://blog.csdn.net/tanzuozhev/article/details/50442243
# 安装
# pip install lxml

# 在Windows上运行,from lxml import etree会报错的问题:
# 1、打开PyCharm设置
# 2、在Project Interpreter下，重新install lxml
# https://blog.csdn.net/qq1815145797/article/details/78394363



# XPath语法 ##########################################
# XPath 是一门在 XML 文档中查找信息的语言。XPath 可用来在 XML 文档中对元素和属性进行遍历。XPath 是 W3C XSLT 标准的主要元素，并且 XQuery 和 XPointer 都构建于 XPath 表达之上。

# nodename	选取此节点的所有子节点。
# /	从根节点选取。
# //	从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
# .	选取当前节点。
# ..	选取当前节点的父节点。
# @	选取属性。

# /bookstore/book[1]	选取属于 bookstore 子元素的第一个 book 元素。
# /bookstore/book[last()]	选取属于 bookstore 子元素的最后一个 book 元素。
# /bookstore/book[last()-1]	选取属于 bookstore 子元素的倒数第二个 book 元素。
# /bookstore/book[position()<3]	选取最前面的两个属于 bookstore 元素的子元素的 book 元素。
# //title[@lang]	选取所有拥有名为 lang 的属性的 title 元素。
# //title[@lang=’eng’]	选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。
# /bookstore/book[price>35.00]	选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。
# /bookstore/book[price>35.00]/title	选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。

# *	匹配任何元素节点。
# @*	匹配任何属性节点。
# node()	匹配任何类型的节点。

# 通过在路径表达式中使用“|”运算符，您可以选取若干个路径。
# //title | //price	选取文档中的所有 title 和 price 元素。

# |	计算两个节点集	//book | //cd	返回所有拥有 book 和 cd 元素的节点集
# +	加法	6 + 4	10
# –	减法	6 – 4	2
# *	乘法	6 * 4	24
# div	除法	8 div 4	2
# =	等于	price=9.80	如果 price 是 9.80，则返回 true。如果 price 是 9.90，则返回 false。
# !=	不等于	price!=9.80	如果 price 是 9.90，则返回 true。如果 price 是 9.80，则返回 false。
# <	小于	price<9.80	如果 price 是 9.00，则返回 true。如果 price 是 9.90，则返回 false。
# <=	小于或等于	price<=9.80	如果 price 是 9.00，则返回 true。如果 price 是 9.90，则返回 false。
# >	大于	price>9.80	如果 price 是 9.90，则返回 true。如果 price 是 9.80，则返回 false。
# >=	大于或等于	price>=9.80	如果 price 是 9.90，则返回 true。如果 price 是 9.70，则返回 false。
# or	或	price=9.80 or price=9.70	如果 price 是 9.80，则返回 true。如果 price 是 9.50，则返回 false。
# and	与	price>9.00 and price<9.90	如果 price 是 9.80，则返回 true。如果 price 是 8.50，则返回 false。
# mod	计算除法的余数	5 mod 2	1


from lxml import etree

# 初步使用
# 首先我们利用它来解析 HTML 代码，先来一个小例子来感受一下它的基本用法。
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result)
# 首先我们使用 lxml 的 etree 库，然后利用 etree.HTML 初始化，然后我们将其打印出来。
# 其中，这里体现了 lxml 的一个非常实用的功能就是自动修正 html 代码，大家应该注意到了，最后一个 li 标签，其实我把尾标签删掉了，是不闭合的。不过，lxml 因为继承了 libxml2 的特性，具有自动修正 HTML 代码的功能


# 文件读取
html = etree.parse('../../files/hello.html')
result = etree.tostring(html, pretty_print=True)
print(result)


# 获取所有的 <li> 标签
html = etree.parse('../../files/hello.html')
print(type(html))
result = html.xpath('//li')
print(result)
print(len(result))
print(type(result))
print(type(result[0]))


# 获取 <li> 标签的所有 class
result = html.xpath('//li/@class')
print(result)


# 获取 <li> 标签下 href 为 link1.html 的 <a> 标签
result = html.xpath('//li/a[@href="link1.html"]')
print(result)


# 获取 <li> 标签下的所有 <span> 标签
# result = html.xpath('//li/span')  # / 是用来获取子元素的，而 <span> 并不是 <li> 的子元素，所以，要用双斜杠
result = html.xpath('//li//span')


# 获取 <li> 标签下的所有 class，不包括 <li>
result = html.xpath('//li/a//@class')
print(result)


# 获取最后一个 <li> 的 <a> 的 href
result = html.xpath('//li[last()]/a/@href')
print(result)


# 获取倒数第二个元素的内容
result = html.xpath('//li[last()-1]/a')
print(result[0].text)


# 获取 class 为 bold 的标签名
result = html.xpath('//*[@class="bold"]')
print(result[0].tag)