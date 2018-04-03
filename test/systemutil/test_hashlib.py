# hashlib  | 摘要算法
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
# 什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。



# MD5
import hashlib
md5 = hashlib.md5()
md5.update("how to use md5 in python hashlib?".encode('utf-8'))
print(md5.hexdigest())

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 封装MD5
def calc_md5(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()
print(calc_md5('123456').upper())

# sha1
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长
sha256 = hashlib.sha256()
sha256.update('how to use sha1 in '.encode('utf-8'))
sha256.update('python hashlib?'.encode('utf-8'))
print(sha256.hexdigest())

sha512 = hashlib.sha512()
sha512.update('how to use sha1 in '.encode('utf-8'))
sha512.update('python hashlib?'.encode('utf-8'))
print(sha512.hexdigest())



# 加盐 | 就是在需要编码的字符串基础上再加上一个Salt，使得难以破解
def calc_md5_salt(password,selt='the-Salt'):
    return hashlib.md5((password + selt).encode('utf-8')).hexdigest()
print(calc_md5_salt('123456','hezhao'))

# 经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。
# 但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，这说明这两个用户的口令是一样的。有没有办法让使用相同口令的用户存储不同的MD5呢？
# 如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。


# 小结
# 摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。