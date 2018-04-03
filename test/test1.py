# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Python3 中有六个标准的数据类型：
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Sets（集合）
Dictionary（字典）
'''

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

# 删除对象的引用
del counter

'''
Python3 支持 int、float、bool、complex（复数）。
注意：在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。
'''
# 判断数据类型
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))

a = 111
print(isinstance(a, int))

'''
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''

str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串


obj = 'I\'m a \"chinese\"!\nand you?'
print(obj)

obj = "jjj" + r'I m a boy'
print(obj)

obj = '''
line1
line2
line3
'''
print(obj)

obj = False
print(obj)

# not and or 逻辑运算符
'''
这是多行注释
使用单引号。
'''

"""
这是多行注释
使用双引号。
"""

if not obj and 1>2 :
    print("这是true")
else:
    print("这是false")

# 多行语句
total = 's' + \
        'o' + \
        's'
print(total)

# 常量
PI = 3.1415926

# 这种除法结果为浮点数
result = 10 / 3
print(result)

# 地板除 结果为整数
result = 10 // 3
print(result)

# 取余
result = 10 % 3
print(result)

# 编码
print(ord('a'))
print(ord('A'))
print(ord('啊'))

print(chr(97))
print(chr(21834))

print('\u4e2d\u6587')


# 编码解码 str 和 byte相互转换
ec = 'ABC'.encode('ascii')
print(ec)

ec = '中文'.encode('utf-8')
print(ec)

code = b'\xe4\xb8\xad\xe6\x96\x87'
zw = code.decode('utf-8')
print(zw)

# 获取长度
print(zw.__len__())
print(len(zw))
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len(code))

# 字符串格式化
# 在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
str = 'Hello,%s' %'HeZhao'
print(str)
print('Hi,%s,you have %d money' %('Jack',100))
# 指定是否补0和整数与小数的位数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
# %%来表示一个%
print('growth rate: %d %%' % 7)


# 判断字符串是否包含某一个字符
# 方法1
site = 'http://www.sharejs.com/'
if "sharejs" in site:
     print('site contains sharejs')

# 方法2
s = "This be a string"
if s.find("is") == -1:
    print("No 'is' here!")
else:
    print("Found 'is' in the string.")

# 方法3
print(s.__contains__('string'))


# 拆分字符串
print('1,2,3,4'.split(','))
# 连接数组
print('-'.join(['A', 'B', 'C', 'D']))


# Python数据类型转换
'''
int(x [,base])      将x转换为一个整数
float(x)            将x转换到一个浮点数
complex(real [,imag])   创建一个复数
str(x)              将对象 x 转换为字符串
repr(x)             将对象 x 转换为表达式字符串
eval(str)           用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)            将序列 s 转换为一个元组
list(s)             将序列 s 转换为一个列表
set(s)              转换为可变集合
dict(d)             创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s)        转换为不可变集合
chr(x)              将一个整数转换为一个字符
unichr(x)           将一个整数转换为Unicode字符
ord(x)              将一个字符转换为它的整数值
hex(x)              将一个整数转换为一个十六进制字符串
oct(x)              将一个整数转换为一个八进制字符串
'''