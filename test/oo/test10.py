# 面向对象编程

# 面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。


# 以一个例子来说明面向过程和面向对象在程序流程上的不同之处。

# std1 = {'name': 'Michael', 'score': 98}
# std2 = {'name': 'Bob', 'score': 81}
#
# def print_score(std):
#     print('%s:%s' % (std['name'],std['score']))
#
# print_score(std1)
# print_score(std2)


# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s: %s' %(self.name, self.score))
#
#
# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
#
# bart.print_score()
# lisa.print_score()


# 1、创建实例是通过类名+()实现的
# 2、__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 3、和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self,并且，调用时，不用传递该参数。
# 4、和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同



# 访问限制
# - 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
# - 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
# - 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
# - 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    # getter
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # setter
    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


bart = Student('Bart Simpson', 59)
bart.print_score()
print(bart.get_name())
bart.set_name('Tom')
bart.set_score(98)
bart.print_score()

#注意， 这里设置的__name和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。
bart.__name = 'abc'
print(bart.get_name())

