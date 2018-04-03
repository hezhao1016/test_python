# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 函数

num = abs(-1)
print('max - %s' %max(-1,0,1,2))
print('min - %s' %min(-1,0,1,2))

print(int('123'))
print(float('1.23'))
print(str(1.23))

# 下面这些都是false
print(bool(None))
print(bool(False))
print(bool(''))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(set()))
print(bool(frozenset()))


# 定义函数
def sub(a,b):
    if not isinstance(a,(int,float)):
        raise TypeError("错误参数类型")
    return a-b

# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。

# 空函数
def nop():
    pass

print(sub(2,1))
# sub('2','1')



import math

# 返回多个值
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x,y = move(100,100,80,math.pi / 6)
print(x,y)

#实际 返回值是一个tuple
r = move(100, 100, 80, math.pi / 6)
print(r)


#-----------复杂参数-------------
print('--------------------------')

# 位置参数
# def power(x):
#     return x * x
# print(power(5))


###################### 默认参数
# 必选参数在前，默认参数在后
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))


# 多个默认参数
def enroll(name, gender, age=6, city='Beijing'):
    print('**************')
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数
# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。
enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')

# !!! 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=[]):
    L.append('END')
    return L


# 正常调用 没有问题
add_end([1, 2, 3])


# 调用两次 结果出错 每次调用都记住了上次做的改变 即 默认参数如果是可变对象，则会记住最后一次修改的值
add_end()
add_end()

'''
Python函数在定义的时候，默认参数L的值就被计算出来了，
即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
'''


# 要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


###################### 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


calc()
calc(1)
calc(1, 2)

# 如果要调用的参数已经是一个数组了 也可以这么写
nums = [1, 2, 3]
calc(*nums)
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。


####################### 关键字参数
print('-----------------------------')


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('张三',18)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# 直接传入dict
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 命名关键字参数 可以限制关键字参数的名字
print('-----------------------------')


# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

# 命名关键字参数必须传入参数名
person('Jack', 24,city='Beijing',job='Engineer')


# 命名关键字参数可以有缺省值
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

# 由于命名关键字参数city具有默认值，调用时，可不传入city参数
person('Jack', 24, job='Engineer')



'''
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''
print('-------------------------')


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)


# 最神奇的是通过一个tuple和dict，你也可以调用上述函数
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的



'''
递归函数
'''
print('------------递归函数-----------')


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(10))

# 理论上任何递归都可以用循环替代
sum = 1
for i in range(10):
    sum *= i+1
print(sum)

