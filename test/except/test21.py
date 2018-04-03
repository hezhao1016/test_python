# 调试、日志


# 断言
# 启动Python解释器时可以用-O参数来关闭assert
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

# main()




# logging
import logging
logging.basicConfig(level=logging.DEBUG)

s = '0'
n = int(s)
logging.debug('n = %d' % n)
print(10 / n)




# pdb
# $ python -m pdb err.py
# 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码
# 输入命令n可以单步执行代码
# 任何时候都可以输入命令p 变量名来查看变量
# 输入命令q结束调试，退出程序

# pdb.set_trace()
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行
