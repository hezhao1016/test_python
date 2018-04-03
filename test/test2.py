# !/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
>> list 列表
'''
print('\n----------------list----------------\n')
arr = [1,2,3,'bob']
# print(arr)

for a in arr:
    print(a)

print("len:%s" % len(arr))

print(arr[len(arr)-1])
# -1 取最后一个元素
print(arr[-1])
print(arr[-2])

# 追加到结尾
arr.append("张三")
arr[-1] = 'zhangsan'
print(arr)

# 追加到指定位置
arr.insert(2,"李四")
print(arr)

# 删除结尾
arr.pop()
print(arr)

# 删除指定位置
arr.pop(1)
print(arr)

arr[0] = True
print(arr)

# 二维数组
aa = ['a','b',['1','2'],'c']
print(aa[2][0])

# 空数组
noneArr = []
print(noneArr)

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)  # 输出完整列表
print(list[0])  # 输出列表的第一个元素
print(list[1:3])  # 输出第二个至第三个元素
print(list[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)  # 输出列表两次
print(list + tinylist)  # 打印组合的列表


'''
>> tuple 元组 ： 一旦初始化不能修改
!! 当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
'''
print('\n----------------tuple----------------\n')
classmates = ("jack","frank","emase")

print(classmates)

# 空元组
t = ()

# 只有一个元素的tuple 必须加逗号
t = (1,)
print(t)

# 最后来看一个“可变的”tuple：
# ps : 和java一样 ::: 对象不能在new，但属性是可变的

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)


'''
>> dict 键值对 字典 对应java里的map 无序
'''
print('\n----------------dict----------------\n')
dict = {'1':"a",
        'list':[
            {'name':'bob','age':18},
            {'name':'bob2','age':18}
        ]
    }
print(dict)
print(dict['list'][0]['name'])


# 学生成绩表
# dict的key必须是不可变对象。 不能放list
scores = {'张三':60,'李四':100,'王五':80}
scores['麻子'] = 0
scores['麻子'] = 20

print(scores)


# 判断键是否存在
flag = '麻子' in scores
print(flag)

# contains 同样的效果
flag2 = scores.__contains__('麻子')
print(flag2)

# 通过dict提供的get方法，如果key不存在，可以返回None，或者返回自己指定的value
flag2 = scores.get('麻子2')
flag3 = scores.get('麻子2','不存在')
print(flag3)

'''
Python中对变量是否为None的判断
三种主要的写法有：
第一种：if X is None;
第二种：if not X；当X为None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()这些时，not X为真，即无法分辨出他们之间的不同。
第二种：if X；和 if not X 相反
第三种：if not X is None;
'''
print(flag2 is None)
print(not flag2)

scores.pop('麻子')
print(scores)

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # 输出键为'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值


'''
>> set 和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。 
'''
print('\n----------------set----------------\n')

# 要创建一个set，需要提供一个list作为输入集合
s = set([1,2,3])
s = {1,2,3}
print(s)

s = set([0,1,2,1,2,3])
print(s)

s.add(4)
s.add(4)
print(s)

s.remove(4)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)
print(s1 | s2)
print(s1.symmetric_difference(s2))


# set 不能存list
# list = [1,2]
# slist = set([list])
# print(slist)

print(1 in s1)

# 只能循环取出
for s in s1:
    print(s)

s1 -= {1,2}
print('-= 之后的 %s' %s1)

s3 = {'abcdefg'}
print(s3)

'''
python中set和frozenset方法和区别
set(可变集合)与frozenset(不可变集合)的区别：
set无序排序且不重复，是可变的，有add（），remove（）等方法。既然是可变的，所以它不存在哈希值。基本功能包括关系测试和消除重复元素. 
    集合对象还支持union(联合), intersection(交集), difference(差集)和sysmmetric difference(对称差集)等数学运算. 
sets 支持 x in set, len(set),和 for x in set。作为一个无序的集合，sets不记录元素位置或者插入点。因此，sets不支持 indexing, 或其它类序列的操作。
frozenset是冻结的集合，它是不可变的，存在哈希值，好处是它可以作为字典的key，也可以作为其它集合的元素。缺点是一旦创建便不能更改，没有add，remove方法。
http://www.cnblogs.com/panwenbin-logs/p/5519617.html
'''
t = frozenset([1,2,3,4])
t = frozenset('12346589')
tx = frozenset('13579')
print(t)

for t1 in t:
    print(t1)

print(t.intersection(tx))


'''
不可变对象
'''
print('\n-----------------------------------\n')

a = ['c','a','b']
a.sort()
print(a)

# 字符串不可变
a = 'abc'
a.replace('a','A')
print(a)





# 练习 在一个列表中，按照日期重新组合数据，相同日期放在同一个列表中
l = [
    {'date':'2018-03-09','name':'tom0'},
    {'date':'2018-03-08','name':'tom1'},
    {'date':'2018-03-09','name':'tom2'},
    {'date':'2018-03-08','name':'tom3'}
]

d = {}

for x in l:
    if x['date'] not in d:
        d[x['date']] = []
    d[x['date']].append(x)

print(d)