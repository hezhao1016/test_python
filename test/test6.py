# 切片
# array = [1,2,3,4,5,6,7,8,9]
array = (1,2,3,4,5,6,7,8,9)
# array = 'ABCDEFGHI'

print(array[0:3])
print(array[:3])
print(array[3:])
print(array[:6:2])
print(array[::2])
print(array[:])


# 使用 切片 实现 trim()

def trim(s):
    if s[:1] == " ":
        return trim(s[1:])
    elif s[-1:] == " ":
        return trim(s[:len(s)-1])
    else:
        return s

print(trim(' 1 '))


def trim2(vstr):
    if(len(vstr)==0 or (vstr[0]!=' ' and vstr[-1]!=' ')):
        return vstr
    else:
        return trim(vstr[0]==' ' and vstr[1:] or vstr[:-1])

print(trim2(' 1 '))


# 迭代
print('---------------------')

d = {'a': 1, 'b': 2, 'c': 3}

# 默认情况下，dict迭代的是key
for key in d:
    print(key)

# 迭代value
for value in d.values():
    print(value)

# 同时迭代key和value
for item in d.items():
    print(item)   # 返回的是一个元组

for k,v in d.items():
    print(k, '=', v)

# 迭代字符串
for s in 'ABC':
    print(s)

# 判断一个对象是可迭代对象
from collections import Iterable

print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))


# 实现下标
for i,value in enumerate('XYZ'):
    print(i,value)

# 同时引用多个变量
for x,y,z in [(1,1,1),(2,4,6),(3,7,9)]:
    print(x,y,z)


# 使用迭代查找一个list中最小值和最大值
def findMinAndMax(L):
    if not L:
        return None,None
    max = L[0]
    min = L[0]
    for j in L:
        if j > max:
            max = j
        if j < min:
            min = j
    return min,max

list1 = [1,3,11,100,54,2,6,2,56]
print(findMinAndMax([]))
print(findMinAndMax(list1))


# 列表生成式
print('------------------------')

# 简单
list2 = list(range(1,11))
print(list2)

# 把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
list3 = [x*x for x in list(range(1,11))]
list4 = [x*x for x in list2]
print(list3)
print(list4)

# 使用if
list5 = [x*x for x in list(range(1,11)) if x % 2 == 0]
print(list5)

#多层循环
list6 = [m + n for m in 'ABC' for n in 'XYZ']
list7 = [m + n + v for m in 'ABC' for n in 'XYZ' for v in '123']
print(list6)
print(list7)

# 列出当前目录下的所有文件名
import os
listdir = [d for d in os.listdir('.')]
print(listdir)

# dict to list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

# 把一个list中所有的字符串变成小写
L = ['MeiZu','Apple','XiaoMi',18,None]
L2 = [s.lower() for s in L if isinstance(s,str)]
L3 = [isinstance(s,str) and s.lower() or s for s in L]
print(L2)
print(L3)


# 生成器

print('--------------生成器-------------')
# 创建列表生成式和生成器的区别仅在于最外层的[]和()，L是一个list，而g是一个generator
g = (x*x for x in range(10))
# print(next(g))

for n in g:
    print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'

print("--------fib-----------")
print(fib(10))


# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

print("--------fib2-----------")
g = fib2(10)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中

def odd():
    print("step 1")
    yield 1
    print("step 3")
    yield 3
    print("step 5")
    yield 5

o = odd()
print(next(o))
print(next(o))
print(next(o))


# 测试 杨辉三角
def triangles(n):
    L = [1]
    while len(L) < n+1:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]

for t in triangles(10):
    print(t)




# 迭代器
# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable

print('===============迭代器==================')
# 可以使用isinstance()判断一个对象是否是Iterable对象：
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance([x for x in range(10)], Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))


# 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 可以使用isinstance()判断一个对象是否是Iterator对象：
print('===========================')
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))


# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]), Iterator))

# 你可能会问，为什么list、dict、str等数据类型不是Iterator？
# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

# 小结
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。


print('==========================')
# Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1, 2, 3, 4, 5]:
    print('for - ', x)

# 实际上完全等价于：

# -------------------------------------------
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print('next - ', x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
# -------------------------------------------

# 以上封装成函数 | 自定义for循环
def myfor(list, func):
    # 首先获得Iterator对象:
    it = iter(list)
    # 循环:
    while True:
        try:
            # 获得下一个值:
            x = next(it)
            func(x)
        except StopIteration:
            # 遇到StopIteration就退出循环
            break

myfor([1, 2, 3, 4, 5], lambda x: print('myfor - ', x))