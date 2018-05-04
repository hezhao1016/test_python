# 函数式编程

# 函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。
#
# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
#
# Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。


# 返回函数
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

print(calc_sum(1,3,5,7,9))
f = lazy_sum(1,3,5,7,9)
print(f())

f1 = lazy_sum(1,3,5,7,9)
print(f == f1)


# 闭包 -- 相关参数和变量都保存在返回的函数中，这种称为 闭包（Closure）
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


def count_1():
    def f(j):
        # return lambda: j * j
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i)) # f(i) 立刻被执行，因此i的当前值被传入f()
    return fs

f4, f5, f6 = count_1()
print(f4())
print(f5())
print(f6())



# 练习 使用闭包实现计数器
print('-----------------------')
def createCounter():
    sum = 0
    def counter():
        nonlocal sum
        sum += 1
        return sum
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')



# 匿名函数
print('-----------------------')
print(list(map(lambda x:x * x,[1,2,3,4,5,6,7,8,9])))
f = lambda x: x * x
print(f(2))

def build(x,y):
    return lambda: x * x + y * y

print(build(2,3)())

L = list(filter(lambda n : n % 2 == 1,range(1,20)))
print(L)



# 装饰器(Decorator)
print('-----------------------')
def now():
    print('2017-12-18')

f = now
print(now.__name__)
print(f.__name__)


import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now_1():
    print('2017-12-18')

now_1()

def log_2(text):
    if(isinstance(text, str)):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s()' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('call %s()' % text.__name__)
            return text(*args, **kw)
        return wrapper

@log_2('iii')
def now_2():
    print('2017-12-18')

now_2()


print('-----------test------------')
import time, functools
def metric(fn):
    def wrapper(*args, **kw):
        s_time = time.time()
        r = fn(*args, **kw)
        e_time = time.time()
        print('%s executed in %s ms' % (fn.__name__, e_time - s_time))
        return r
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')




# 偏函数
print('--------偏函数--------')

int('12345')
def int2(x,base=2):
    return int(x,base)

print(int2('1000000'))

# functools.partial 帮助我们创建一个偏函
import functools
int2 = functools.partial(int,base=2)

print(int2('1000000'))


# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

max2 = functools.partial(max, 10)
print(max2(5, 6, 7))



