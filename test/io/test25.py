# 操作文件和目录

import os

# posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.name)

# 环境变量
print(os.environ)
print(os.environ.get('PATH'))
print(os.environ.get('x', 'default'))


# 查看当前目录绝对路径
print(os.path.abspath('F:/xdir'))
# 把新目录的完整路径表示出来:
path = os.path.join('F:/xdir', 'testdir')
print(path)
# 创建一个目录:
os.mkdir(path)
# 删掉一个目录:
os.rmdir('F:/xdir/testdir')

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# 拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
path = os.path.split('/Users/michael/testdir/file.txt')
print(path)

# os.path.splitext()可以直接让你得到文件扩展名
print(os.path.splitext('/path/to/file.txt'))

# >>>这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作



# 对文件重命名
# os.rename('F:/xdir/test.txt', 'F:/xdir/test.py')
# 删掉文件:
# os.remove('test.py')


#自己实现复制文件
def copy(sourcePath,targetPath):
    if(os.path.isfile(sourcePath) == False):
        raise IOError('未找到相关文件[%s]' % sourcePath)

    # 如果目标文件存在，先删除
    if (os.path.isfile(targetPath)):
        os.remove(targetPath)

    with open(sourcePath,'r') as sourceFile:
        with open(targetPath,'a') as targetFile:
            while True:
                temp = sourceFile.read(1024)
                if (temp == ''):
                    break
                targetFile.write(temp)

# copy('F:/xdir/abc.txt','F:/xdir/123.txt')


# 另一种复制文件
import shutil
# shutil.copyfile('F:/xdir/abc.txt','F:/xdir/123.txt')


# 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# 练习 在指定目录以及指定目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
path = 'F:/workspace/'
word = 'payadmin'

def searchFile(path,word):
    for dir in os.listdir(path):
        newDir = os.path.join(path, dir)
        if os.path.isdir(newDir):
            searchFile(newDir,word)
        if word in dir:
            print(newDir)

searchFile(path,word)


# ---------------------------------------------检查文件是否存在
print('========================')

# 1、使用os模块
import os
flag = os.path.exists('F:/abc.txt')  # 是否存在
print(flag)

isfile = os.path.isfile('F:/abc.txt')  # 是否是文件
print(isfile)

isdir = os.path.isdir('F:/')  # 是否是目录
print(isdir)

# 判断文件是否可做读写操作
# os.access(path, mode)
# path为文件路径，mode为操作模式，有这么几种:

# os.F_OK: 检查文件是否存在;
# os.R_OK: 检查文件是否可读;
# os.W_OK: 检查文件是否可以写入;
# os.X_OK: 检查文件是否可以执行

# 该方法通过判断文件路径是否存在和各种访问模式的权限返回True或者False。

if os.access("F:/abc.txt", os.F_OK):
    print("Given file path is exist.")

if os.access("F:/abc.txt", os.R_OK):
    print("File is accessible to read")

if os.access("F:/abc.txt", os.W_OK):
    print("File is accessible to write")

if os.access("F:/abc.txt", os.X_OK):
    print("File is accessible to execute")

# 2、使用try except [IOError]

# 3、使用pathlib模块

# ---------------------------------------------检查文件是否存在