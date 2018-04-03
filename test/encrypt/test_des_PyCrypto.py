from Crypto.Cipher import DES3
import base64

# 明文必须为8的倍数
def align_val(content):
    if not content:
        return content
    if len(content) % 8 != 0:
        zerocount = 8 - len(content) % 8
        for i in range(0, zerocount):
            content += '\0'
        return content
    else:
        return content

# 密码为16位或者24位
def align_key(key):
    if not key or len(key) == 16 or len(key) == 24:
        return key
    if len(key) < 16:
        count = 16
    elif len(key) < 24:
        count = 24
    else:
        return key[:24]
    zerocount = count - len(key) % count
    for i in range(0, zerocount):
        key += '\0'
    return key



iv = ''.join([chr(val) for val in [0x12, 0x34, 0x56, 0x78, 0x90, 0xAB, 0xCD, 0xEF]])
key = align_key('123456')
val = align_val('Hello')

obj = DES3.new(key, DES3.MODE_ECB, iv)

t = base64.b64encode(obj.encrypt(val))
print(t)
t = obj.decrypt(base64.b64decode(t)).decode('utf-8')
print(t)

