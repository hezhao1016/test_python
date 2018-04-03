# itertools | 操作迭代对象

import itertools

# natuals = itertools.count(1)
# for n in natuals:
#     print(n)
# count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出


# cycle()会把传入的一个序列无限重复下去
# cs = itertools.cycle('ABC')  # 注意字符串也是序列的一种
# for c in cs:
#     print(c)


# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat("A", 3)
for n in ns:
    print(n)


# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))



# itertools提供的几个迭代器操作函数更加有用：
#
# chain()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in  itertools.chain('ABC', 'XYZ'):
    print(c)


# groupby()
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

for key ,group in itertools.groupby('AaABbBbCcAaa', lambda c: c.upper()):
    print(key, list(group))



# 练习 计算圆周率
def pi(N):
    #直接用count即可，从1开始每项加2
    odd=itertools.count(1,2)
    #用takewhile取出前N项
    needed=itertools.takewhile(lambda x:x<2*N,odd)
    list=[x for x in needed]
    #分别求和
    return (sum(4/x for x in list if x%4==1)+sum(-4/x for x in list if x%4==3))
print(pi(100000))


# 小结
# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。

