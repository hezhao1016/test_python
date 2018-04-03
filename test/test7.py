# ------------------------------------------------------ 高阶函数

# 变量可以指向函数
f = abs
print(f)
print(f(-10))


# 函数名也是变量
# abs = 10
# abs(-10)


# 把函数作为参数 这称之为 "高阶函数"
def add(x,y,f):
    return f(x) + f(y)


print(add(-5,6,abs))



# ------------------------------------------------------ map/reduce
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
print('-------------------------')
def f(x):
    return x * x

nums = [1,2,3,4,5,6,7,8,9]
print(list(map(f,nums)))

def toStr(s):
    return str(s)

print(list(map(toStr,nums)))


print('-------------------------')
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce


def add(x,y):
    return x + y

print(reduce(add,[1,3,5,7,9]))


def fn(x,y):
    return x * 10 + y

print(reduce(fn,[1,3,5,7,9]))


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn, map(char2num, '13579')))


# 加以改造

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


print(str2int('674556'))


# lambda简化
def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(str2int('524132'))



print('------------练习1--------------')
def normalize(name):
    return name[:1].upper() + name[1:].lower()

print(list(map(normalize,['LISA','soa','tOM'])))


print('------------练习2--------------')
def prod(x,y):
    return x * y

print(reduce(prod,[1,3,5,6]))


print('------------练习3--------------')

def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    def power10(n):
        if n == 0:
            return 1
        if n == 1:
            return 10
        return 10 * power10(n - 1)

    def str2num(x, y):
        return x * 10 + y

    if '.' in s:
        indexDot=s.index('.')
        listS=list(s)
        listS.remove('.')
    else:
        indexDot=len(s)-1
        listS=list(s)
    return reduce(str2num,map(char2num,listS))/(power10(len(s)-indexDot-1))

print(str2float('123.456'))




# ------------------------------------------------------ filter
# filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
print('--------------filter-------------')

def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
print(list(filter(lambda n:  n % 2 == 1, [1, 2, 4, 5, 6, 9, 10, 15])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))



# 筛选所有素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break


# ------------------------------------------------------ sorted
print('-------------------sorted-----------------')

arr = [36, 5, -12, 9, -21]
arr2 = sorted(arr)
print(arr)
print(arr2)

# 也可以使用list.sort()方法来排序，此时list本身将被修改。通常此方法不如sorted()方便，但是如果你不需要保留原来的list，此方法将更有效。
# sorted不会修改原列表，只是返回排序后的列表
a = [5, 2, 3, 1, 4]
print(a.sort())  # 返回 None 来避免混淆
print(a)

arr = sorted([36, 5, -12, 9, -21], key=abs)
print(arr)

arr = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(arr)

# 练习 用sorted()对学生列表分别按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

L2 = sorted(L, key=lambda x: x[0].lower())
print(L2)

res = sorted(L, key=lambda x: -x[1])
print(res)


# 常用七种排序的python实现 | https://www.cnblogs.com/zingp/p/6537841.html
# 冒泡排序实现

arr = [3, 6, 7, 2, 9, 2, -4, 12]
for i in range(len(arr) - 1):
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
