# 正则表达式

# re模块

# Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义，所以要特别注意：

# s = 'ABC\\-001' # Python的字符串
# # 对应的正则表达式字符串变成：
# 'ABC\-001'

# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：
# s = r'ABC\-001' # Python的字符串
# 对应的正则表达式字符串不变：
# 'ABC\-001'

# 判断正则表达式是否匹配
import re
reg = r'\d{3}\-\d{3,8}$'
result = re.match(reg, '010-12345')
print(result)
result = re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
print(result)
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。

# 常见的判断方法就是：
# test = '用户输入的字符串'
# if re.match(r'正则表达式', test):
#     print('ok')
# else:
#     print('failed')


# 切分字符串
print(re.split(r'\s+', 'a b  c'))
print(re.split(r'[\s\,]+', 'a,b, c  d'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))


# 分组
# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。
# 比如： ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码
# 如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
# 注意到group(0)永远是原始字符串[贪婪匹配的最大长度]，group(1)、group(2)……表示第1、2、……个子串。
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

t = '19:05:30'
m = re.match(
    r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    t)
print(m.groups())  # 所有元素


# 贪婪匹配 | 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。

print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())


# 编译
# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
# 1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 2. 用编译后的正则表达式去匹配字符串。

# 预编译
import re
# 编译:
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
print(re_telephone.match('010-12345').groups())  # 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。
print(re_telephone.match('010-8086').groups())




# 练习
# 题1：验证Email

import re

reg_email = r'^([0-9a-zA-Z]+[\.\_]?[0-9a-zA-Z]*)@[0-9a-zA-Z\.\-]+\.[a-zA-Z]{2,4}$'

def is_valid_email(addr):
    m = re.compile(reg_email)
    if m.match(addr) is None:
        return False
    return True

reg_name_of_email = r'^<([\w\s]+)>[\s]*([0-9a-zA-Z]+[\.\_]?[0-9a-zA-Z]*)@[0-9a-zA-Z\.\-]+\.[a-zA-Z]{2,4}$'

# 题2：提取出带名字的Email地址 | <Tom Paris> tom@voyager.org => Tom Paris
def name_of_email(addr):
    m = re.match(reg_email, addr)
    if m:
        return m.group(1)
    m = re.match(reg_name_of_email, addr)
    if m:
        return m.group(1)
    return None


# 题目一
print('is_valid_email(\'1234567890@qq.com\') = %s' % is_valid_email('1234567890@qq.com'))
print('is_valid_email(\'someone@163.com\') = %s' % is_valid_email('someone@163.com'))
print('is_valid_email(\'someone@gmail.com\') = %s' % is_valid_email('someone@gmail.com'))
print('is_valid_email(\'bill.gates@microsoft.com\') = %s' % is_valid_email('bill.gates@microsoft.com'))
print('is_valid_email(\'bob#example.com\') = %s' % is_valid_email('bob#example.com'))
print('is_valid_email(\'mr-bob@example.com\') = %s' % is_valid_email('mr-bob@example.com'))

# 题目二
print('name_of_email(\'<Tom Paris> tom@voyager.org\') = %s' % name_of_email('<Tom Paris> tom@voyager.org'))
print('name_of_email(\'tom@voyager.org\') = %s' % name_of_email('tom@voyager.org'))

