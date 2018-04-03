# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import os

# 条件判断

# 获取用户输入
# ageStr = 12
ageStr = input('请输入年龄: ')

try:
    age = int(ageStr) #python 没有块级作用域 参考：http://python.jobbole.com/86465/
except:
    print('年龄输入错误')
    # os._exit(0)
    sys.exit(0)
    # sys.exit()的退出比较优雅，调用后会引发SystemExit异常，可以捕获此异常做清理工作。os._exit()直接将python解释器退出，余下的语句不会执行。

if age >= 18:
    print('你是成人')
elif age >= 12:
    print('青少年')
    if age%2 == 0: # 嵌套if
        print("偶数")
    else:
        print('奇数')
else:
    pass # 没什么含义 用来占位置



# 循环
print("--------------------")
for i in range(3):
    print(i)

# range 转 list
list = list(range(10))
print(list)

i = 0
while i<10:
    i+=1
    print(i)
    if i>=3:
        break # break语句会结束当前循环

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print("奇数 %s" %n)

# while 1>0:
#     print("死循环了..")
# 用Ctrl+C退出程序


# 九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('%s*%s=%s ' % (j, i, i*j), end='')  # end='' 表示不换行， 默认 \n
    print('')
