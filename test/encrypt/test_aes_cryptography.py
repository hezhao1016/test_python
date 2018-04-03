#! /usr/bin/env python
# -*- coding: utf-8 -*-

# python(3.x) 实现AES 加解密
# 首先 安装cryptography
# pip install cryptography
# 确认安装的是2.x.x版本 (1.x版本的api是不一样的)

# https://segmentfault.com/a/1190000012968005


import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64

# 128bits block size
aes_block_size = 16


# 生成一个随机的密钥
def get_random_key_readable(key_size=256):
    """
    注意要使用密码学安全的随机方法os.urandom.
    这里生成的是str而不是bytes, 为了可读性
    get random key for symmetric encryption
    with key_size bits
    :param key_size: bit length of the key
    :return: bytes key
    """
    # length for urandom
    ulen = int(key_size/8/4*3)
    key = base64.b64encode(os.urandom(ulen))
    return key

# 采用AES CBC 加密
def aes_cbc_encrypt(message, key):
    """
    内容加密前需要padding到128bit(16bytes)的整数倍长度才可. cryptography有对应padding方法.
    初始向量为16bit长度. 返回初始向量+加密数据
    use AES CBC to encrypt message, using key and init vector
    :param message: the message to encrypt
    :param key: the secret
    :return: bytes init_vector + encrypted_content
    """
    iv_len = aes_block_size
    assert type(message) in (str, bytes)
    assert type(key) in (str, bytes)
    if type(message) == str:
        message = bytes(message, 'utf-8')
    if type(key) == str:
        key = bytes(key, 'utf-8')
    backend = default_backend()
    iv = os.urandom(iv_len)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message) + padder.finalize()
    enc_content = encryptor.update(padded_data) + encryptor.finalize()
    return iv + enc_content

# 解密方法
def aes_cbc_decrypt(content, key):
    """
    use AES CBC to decrypt message, using key
    :param content: the encrypted content using the above protocol
    :param key: the secret
    :return: decrypted bytes
    """
    assert type(content) == bytes
    assert type(key) in (bytes, str)
    if type(key) == str:
        key = bytes(key, 'utf-8')
    iv_len = aes_block_size
    assert len(content) >= (iv_len + 16)
    iv = content[:iv_len]
    enc_content = content[iv_len:]
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    unpadder = padding.PKCS7(128).unpadder()
    decryptor = cipher.decryptor()
    dec_content = decryptor.update(enc_content) + decryptor.finalize()
    real_content = unpadder.update(dec_content) + unpadder.finalize()
    return real_content


# # 我们可以随机生成一些message测试下加解密
# import random
# import unittest
# import time
#
# class TestAESEnc(unittest.TestCase):
#
#     def test_aes_enc_dec(self):
#         key = get_random_key_readable()
#         print('开始测试，key is: ', key)
#         total_len = 0
#         s = time.time()
#         for i in range(100):
#             mlen = random.randint(1, 1024*1024)
#             total_len += mlen
#             message = os.urandom(mlen)
#             enc = aes_cbc_encrypt(message, key)
#             dec = aes_cbc_decrypt(enc, key)
#             self.assertEqual(message, dec, 'aes message len {} is not equal'.format(mlen))
#         e = time.time()
#         print('total_len', total_len)
#         print('total_time', e - s)
#         print('speed', total_len / (e - s))
#
# if __name__ == '__main__':
#     unittest.main()


# 注意这里的速度测试是不准的, 因为包含了urandom的时间, 而这个方法比较耗时.
# 但是仍然可以看到, AES的加解密速度是极快的


key = get_random_key_readable()
print(key)
# encrypt来加密我的数据,然后进行base64编码
encodeStr = base64.b64encode(aes_cbc_encrypt('Hello', key))
print(encodeStr)

# 先用base64解密，然后aes解密
print(aes_cbc_decrypt(base64.b64decode(encodeStr), key).decode('utf-8'))
