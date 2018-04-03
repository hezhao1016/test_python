# StringIO

# 很多时候，数据读写不一定是文件，也可以在内存中读写。
# StringIO顾名思义就是在内存中读写str。

from io import StringIO
f = StringIO()
f.write('hello')
print(f.write(' '))
f.write('world!')

print(f.getvalue())


# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())




print('====================')
# BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())


f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())