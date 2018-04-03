# 文件读写


print('========================')
# 读文本 UTF-8
# 标示符'r'表示读,默认r
# 如果文件不存在，open()函数就会抛出一个IOError的错误
try:
    file = open('F:/abc.txt','r')

    print("文件名为: ", file.name)

    # str = file.read() # 读取所有
    # print(str)

    # for line in file.readlines():  # 一次读取所有内容并按行返回list
    #     print(line.strip())  # 把末尾的'\n'删掉

    # done = 0
    # while not done:
    #     aLine = file.read(2)  # 按字节读取
    #     if (aLine != ''):
    #         print(aLine.strip())
    #     else:
    #         done = 1

    while True:
        aLine = file.readline()  # 读取一行
        if (aLine == ''):
            break
        print(aLine.strip())

except IOError as e:
    print('IOError:', e)
finally:
    if file:
        file.close()


print('========================')
with open('F:/abc.txt') as file:  # 自动调用close()
    print(file.read())

# 可以直接迭代file
print('==========直接迭代file==============')
with open('F:/abc.txt') as file:
    for line in file:
        print(line.strip())  # 每次打印一行


print('========================')
# 二进制文件
f = open('F:/abc.png', 'rb')  # rb 表示打开二进制文件
print(f.read())


# 设置字符编码
f = open('F:/edf.txt', 'r', encoding='gbk')
print(f.read())

# open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
f = open('F:/edf.txt', 'r', encoding='gbk', errors='ignore')



# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件 , 'a' 表示追加
f = open('F:/123.txt','a',encoding='UTF-8')
# f.write('Hello, 何钊!\n')
f.writelines(['Hello, 何钊!\n','你好，世界！\n'])
f.close()  # 关闭时写入文件
print('写入成功')

# r+、w+、a+ 表示读写都可以，其他的只能读或者写入
# r 只能读，若文件不存在，报错
# r+ 可读可写，若文件不存在，报错
# w  从顶部开始写 会覆盖之前此位置的内容。若文件不存在，创建。
# w+ 可读可写，若文件不存在，创建。会将文件内容清零
# w  只能写 覆盖整个文件 不存在则创建
# a  只能写 从文件底部添加内容 不存在则创建
# a+ 可读可写 从文件顶部读取内容 从文件底部添加内容 不存在则创建