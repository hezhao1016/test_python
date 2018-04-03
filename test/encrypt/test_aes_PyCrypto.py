#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyCrypto是一款非常实用的Python加密模块。但是PyCrypto项目已经于2015年7月停止了
# 网上可以找到预编译的pycrypto安装文件。[但是python3.3以上不支持] - 地址为：http://www.voidspace.org.uk/python/modules.shtml#pycrypto

# !!!发现个好方法 - https://blog.csdn.net/yyd19921214/article/details/54576801
# 有人在github上自己编译了一份，经过测试是可以使用的。https://github.com/sfbahr/PyCrypto-Wheels
# 安装命令如下：
# pip install --use-wheel --no-index --find-links=https://github.com/sfbahr/PyCrypto-Wheels/raw/master/pycrypto-2.6.1-cp35-none-win_amd64.whl pycrypto
# 已经下载好了一个，放在/lib/pycrypto-2.6.1.dist-info-py3.5.zip

# 另外，安装一个关于字符转换的模块
# pip install binascii

# https://blog.csdn.net/u013578500/article/details/77905924



# 要调用PyCrypto的AES加密模块，首先导入AES的包，另外为了确保编码的统一，我选择将密文保存为16进制，因此还需要从binascii中导入b2a_hex和a2b_hex。
from Crypto.Cipher import AES
from binascii import b2a_hex
from binascii import a2b_hex

DEFAULT_IV = '1234567890123456'

# 补全字符
def align(str, isKey=False):
    """
    AES有三种密钥长度16(*AES-128*), 24 (*AES-192*), 和 32 (*AES-256*)，在对字符进行加密时，密码和明文长度必须为16,24,或32。
    因此要对密码和明文进行预处理，确保密码长度为16,24或32，明文长度为16,24或32的整数倍
    这里以16(*AES-128*)为例
    :param str:要加密的字符串
    :param isKey:是否需要密钥
    :return:
    """
    # 如果是密码，需要确保其长度为16
    if isKey:
        if len(str) > 16:
            return str[0:16]
        else:
            return align(str)
            # 如果是被加密字符串或长度不足的密码，则确保其长度为16的整数倍
    else:
        zerocount = 16 - len(str) % 16
        for i in range(0, zerocount):
            str = str + '\0'
        return str


# ECB模式加密
def encrypt_ECB(str, key):
    """
    这里加密函数的流程是：预处理密码和明文->初始化AES->加密->转码->输出结果，代码如下
    这里使用的是ECB的加密模式，关于加密模式，AES共有五种加密模式（ECB，CBC，PCBC，CFB，OFB，CTR）
    ECB模式比较简单，并且安全性相对较差。又称电子密码本模式：Electronic codebook，是最简单的块密码加密模式，加密前根据加密块大小（如AES为128位）分成若干块，之后将每块使用相同的密钥单独加密，解密同理。
    :param str:要加密的字符串
    :param key:密钥
    :return:
    """
    # 补全字符串
    str = align(str)
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_ECB)
    # 加密
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)


# ECB模式解密
def decrypt_ECB(str, key):
    """
    这里解密的流程是：预处理密码->初始化AES->转码->解密->输出结果，代码如下
    :param str:要解密的字符串
    :param key:密钥
    :return:
    """
    # 补全字符串
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_ECB)
    # 解密
    paint = AESCipher.decrypt(a2b_hex(str))
    # 去除/0
    paint = paint.decode('utf-8').rstrip('\0')
    return paint


# CBC模式加密
def encrypt_CBC(str, key, IV=DEFAULT_IV):
    """
    大部分场景下，我们会使用CBC模式来进行AES加密。
    和ECB相比，CBC引入了初始向量IV（Initialization vector），每一次加密都使用随机产生的初始向量可以大大提高密文的安全性（这里的示例代码使用固定的IV），代码如下。
    :param str:要加密的字符串
    :param key:密钥
    :param IV:向量IV
    :return:
    """
    # 补全字符串
    str = align(str)
    key = align(key, True)
    # 初始化AES，引入初始向量
    AESCipher = AES.new(key, AES.MODE_CBC, IV)
    # 加密
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)


# CBC模式解密
def decrypt_CBC(str, key, IV=DEFAULT_IV):
    """
    CBC模式解密
    :param str:要解密的字符串
    :param key:密钥
    :param IV:向量IV
    :return:
    """
    # 补全字符串
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_CBC, IV)
    # 解密
    paint = AESCipher.decrypt(a2b_hex(str))
    # 去除/0
    paint = paint.decode('utf-8').rstrip('\0')
    return paint


# CFB模式加密
def encrypt_CFB(str, key, IV=DEFAULT_IV):
    """
    密文反馈（CFB，Cipher feedback）模式与ECB和CBC模式只能够加密块数据不同，可以将块密码变为自同步的流密码；CFB的解密过程几乎就是颠倒的CBC的加密过程。
    :param str:要加密的字符串
    :param key:密钥
    :param IV:向量IV
    :return:
    """
    # 补全字符串，虽然明文长度没有限制，但是密码仍然需要16位
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_CFB, IV)
    # 加密
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)


# CFB模式解密
def decrypt_CFB(str, key, IV=DEFAULT_IV):
    """
    CFB模式解密
    :param str:要解密的字符串
    :param key:密钥
    :param IV:向量IV
    :return:
    """
    # 补全字符串
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_CFB, IV)
    # 解密
    paint = AESCipher.decrypt(a2b_hex(str))
    # 去除/0
    paint = paint.decode('utf-8').rstrip('\0')
    return paint


# OFB模式加密
def encrypt_OFB(str, key, IV=DEFAULT_IV):
    """
    OFB模式（输出反馈：Output feedback），OFB是先用块加密器生成密钥流（Keystream），然后再将密钥流与明文流异或得到密文流，解密是先用块加密器生成密钥流，再将密钥流与密文流异或得到明文，由于异或操作的对称性所以加密和解密的流程是完全一样的。
    :param str:加密字符串
    :param key:密钥
    :param IV:向量IV
    :return:
    """
    # 补全字符串
    str = align(str)
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_OFB, IV)
    # 加密
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)


# OFB模式解密
def decrypt_OFB(str, key, IV=DEFAULT_IV):
    """
    OFB模式解密
    :param str:要解密的字符串
    :param key:密钥
    :param IV:向量IV
    :return:
    """
    # 补全字符串
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_OFB, IV)
    # 解密
    paint = AESCipher.decrypt(a2b_hex(str))
    # 去除/0
    paint = paint.decode('utf-8').rstrip('\0')
    return paint


# 先设置一段明文和密码
Text = 'Hello'
key = '123456'

# ECB模式加密
ciphertext = encrypt_ECB(Text, key)
print("ECB模式密文：", ciphertext)
# ECB模式解密
plaintext = decrypt_ECB(ciphertext, key)
print("ECB模式明文：", plaintext)

# CBC模式加密
ciphertext = encrypt_CBC(Text, key)
print("CBC模式密文：", ciphertext)
# CBC模式解密
plaintext = decrypt_CBC(ciphertext, key)
print("CBC模式明文：", plaintext)

# CFB模式加密
ciphertext = encrypt_CFB(Text, key)
print("CFB模式密文：", ciphertext)
# CFB模式解密
plaintext = decrypt_CFB(ciphertext, key)
print("CFB模式明文：", plaintext)

# OFB模式加密
ciphertext = encrypt_OFB(Text, key)
print("OFB模式密文：", ciphertext)
# OFB模式解密
plaintext = decrypt_OFB(ciphertext, key)
print("OFB模式明文：", plaintext)
