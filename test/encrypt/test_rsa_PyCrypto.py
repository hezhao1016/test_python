# RSA | 公钥加密和签名
# https://www.cnblogs.com/huxianglin/p/6387045.html

# http://www.codeweblog.com/%E4%BF%AE%E5%A4%8D%E5%9C%A8python3%E4%B8%ADimport-winrandom%E9%94%99%E8%AF%AF/
# 问题：在windows的python3使用PyCrypto出现ImportError: No module named 'winrandom'错误
# 处理：修改python3安装目录下的 lib/Crypto/Random/OSRNG/nt.py 文件中找到
# import winrandom
# 修改为
# from Crypto.Random.OSRNG import winrandom


# RSA的公私钥生成
from Crypto import Random
from Crypto.PublicKey import RSA


# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)

# master的秘钥对的生成
private_pem = rsa.exportKey()

#--------------------------------------------生成公私钥对文件-----------------------------------------------------------
with open('../../files/master-private.pem', 'wb') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('../../files/master-public.pem', 'wb') as f:
    f.write(public_pem)

#---------------------------------------------------
# ghost的秘钥对的生成
private_pem = rsa.exportKey()
with open('../../files/ghost-private.pem', 'wb') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('../../files/ghost-public.pem', 'wb') as f:
    f.write(public_pem)

'''
#-----------------------------------生成的公私钥文件类似于如下形式-------------------------------------------------------
# 私钥
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQC6mwuOxuqYi6mugLGr3OuiHwm/hF4kQX1zd5VhGwxYf4H5+pkO
CES2UjOyLP9Xh6w+DJtRwTGE2xwDd3wMfW2wkHijM/uHkM9Jt+oRGIjy4IiXo+7t
ue/NWBkDiQm1qte0YDKlmkFREwvZ5X2KaCsSx+dyKH4QsovxQ3/RxftdmQIDAQAB
AoGAPA5SNe1G6zlnrsW0aL99Bnw+wuhy8/Av082Uwd/WpVTEHBPO1nlKw/LIuHtK
4nzDrmSYSEOJEF0EMwltXwevGSm1wq2FBhX4T+kz3XUpWfv9O0dlHeNtgxeD1QXL
kOxqU4F2WpdALgvi/rlPDd0aIagoXLi8MXkUH7hQlrJpQUECQQC6rygx3jDQA9Iw
kPUXlokEuLod+Kgoa700S5qpJi7vft675+tMG5SZtr+HQeqGHty0fqc8MIcy1fJm
ZYUrogN9AkEA/+RrrOoTYQbR3ENslTsNsiqQa2aZW5XAv9pEyGJBWu/4HUEEa6G3
FY0Y3ACZR0Xaraya8XAgOo61pWm83GBlTQJBAKH2812Ikzr2BbdDHJExdoEVL8xu
/p3LE6U6bt2QFiqNHPtT9C3cw+k0xyi3RJzGS9+A/uDWjYXKXvr92zMG5hUCQFXR
alccTZF9swX2ysSlgGtfIP4T85ymdXUiI208noR79C8DbhMWsgsVPeASh1VC1Rrn
xzLvkq9wyvSFqKQT5AUCQAxMO7KI1rwIm+ISuDEcwxRJXkdFypD74kOSYRxTqMun
Zdu4ku4t6mVeq5kBv1/S2dtF3TiqMRlxmLmV/fx7KHM=
-----END RSA PRIVATE KEY-----

#公钥
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC6mwuOxuqYi6mugLGr3OuiHwm/
hF4kQX1zd5VhGwxYf4H5+pkOCES2UjOyLP9Xh6w+DJtRwTGE2xwDd3wMfW2wkHij
M/uHkM9Jt+oRGIjy4IiXo+7tue/NWBkDiQm1qte0YDKlmkFREwvZ5X2KaCsSx+dy
KH4QsovxQ3/RxftdmQIDAQAB
-----END PUBLIC KEY-----
'''


# RSA使用公私钥加解密数据

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64

message = 'hello ghost, this is a plian text'
with open('../../files/ghost-public.pem',"r") as f:
     key = f.read()
     rsakey = RSA.importKey(key)  # 导入读取到的公钥
     cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
     cipher_text = base64.b64encode(cipher.encrypt(message.encode(encoding="utf-8")))  # 通过生成的对象加密message明文，注意，在python3中加密的数据必须是bytes类型的数据，不能是str类型的数据
     print(cipher_text)

with open('../../files/ghost-private.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)  # 导入读取到的私钥
    cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
    text = cipher.decrypt(base64.b64decode(cipher_text), "ERROR")  # 将密文解密成明文，返回的是一个bytes类型数据，需要自己转换成str
    print(text)
# 结果：
# b'meBtYXP35VNjtWXsONDluweXdG98tMHjb5GxBLFJ0GJzo+96wSrHe8SDhNJweDJP6/OdeIQ8jP1HKCK+aC9HA12YMSUUqcixsY5s8QUyTs+fkMjGrlC6I7hPLO4DGQbFXEY0jiqP9ycgmAi5FCsDMcm0oEm8/fVzv7vl9QarSN4='  # 加密后的密文
# b'hello ghost, this is a plian text'  # 解密后的明文
