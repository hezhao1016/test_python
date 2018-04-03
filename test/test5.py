#---------------------------作用域-------------------------------

# #终极版作用域
#
# name = "lzl"
#
# def f1():
#     print(name)
#
# def f2():
#     name = "eric"
#     f1()
#     print(name)
#
# f2()



# # 作用域链
#
# name = "lzl"
#
# def f1():
#     name = "Eric"
#
#     def f2():
#         name = "Snor"
#         print(name)
#     f2()
#
#     print(name)
#
# f1()
# print(name)



# LEGB含义解释：
# L-Local(function)；函数内的名字空间
# E-Enclosing function locals；外部嵌套函数的名字空间(例如closure)
# G-Global(module)；函数定义所在模块（文件）的名字空间
# B-Builtin(Python)；Python内置模块的名字空间
#




# # 那到底怎么修改全局变量呢？
# #
# # 答案是：运用global与nonlocal.
# #
# # 当变量在全局作用域上的时候，可以这么使用：
# print('----------')
# x = 1
# def outfx():
#     global x  #global改变了G区变量
#     x = 2
# outfx()
# print(x)
#
# # 当变量在父作用域的时候，必须这么使用：
# def outfx():
#     x = 1
#     def infx():
#         nonlocal x  #nonlocal改变了E区变量
#         x = 2
#         print(x)
#     infx()
#     print(x)
# outfx()




# # lambada 面试题
#
# li = [lambda: x for x in range(10)]
#
# print(li.__len__())
#
# print(type(li))
# print(type(li[0]))
#
# res = li[0]()
# print(res)
#
# # 输出：9

#range(0,5,1) 返回一系列连续增加的整数