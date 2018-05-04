# 面向对象高级编程

class Student(object):
    pass

s = Student()
s.name = 'Bob'
print(s.name)

def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(12)
print(s.age)


def set_score(self,score):
    self.score = score

Student.set_score = set_score  # 给类绑定方法


s.set_score(100)
s2 = Student()
s2.set_score(60)

print(s.score)
print(s2.score)


# 使用__slots__

class Student2(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student2() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
# s.score = 99 # 绑定属性'score'


# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
class GraduateStudent(Student2):
    __slots__ = ('score')  # 用tuple定义允许绑定的属性名称
    pass

g = GraduateStudent()
g.score = 9999
g.age = 9
# g.age2 = 9