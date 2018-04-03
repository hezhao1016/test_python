#! /usr/bin/env python
# -*- coding: utf-8 -*-

# pyDES 是一个Python的模块，用来提供 DES、Triple-DES 的加密算法。
# 首先 安装 pyDes
# pip install pyDes

# https://www.cnblogs.com/chjbbs/p/6692170.html


# 使用示例
from pyDes import *
import base64

data = "Hello,World!"  # 要加密的元素
Des_Key = "123abc@*"  # Key
Des_IV = "\0\0\0\0\0\0\0\0"  # IV向量

'''
pyDes.des(key,[mode],[IV],[pad],[padmode])
参数的意思分别如下:
key 加密密钥.长度为8位,必选
mode 加密方式.ECB(默认),CBC(安全性好于前者)
IV  初始字节数(长度为8位),如果你选择的加密方式为CBC就必须有这个参数,否则可以没有
pad 加密时,将该字符添加到数据块的结尾;解密时,将删除从最后一个的往前8位
padmode PAD_NORMAL\PAD_PKCS5,当选择前者时必须设置pad
'''

k = des(Des_Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)
d = k.encrypt(data)  # 加密
print("加密结果: %r" % d)
print("解密结果: %r" % k.decrypt(d))  # 解密
assert k.decrypt(d, padmode=PAD_PKCS5).decode('utf-8') == data

# encrypt来加密我的数据,然后进行base64编码
encodeStr = base64.b64encode(d)
print("DES+base64加密结果", encodeStr)
# 先用base64解密，然后des解密
print("DES+base64解密结果", k.decrypt(base64.b64decode(encodeStr)).decode('utf-8'))
