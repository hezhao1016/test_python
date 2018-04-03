# 获取对象信息


print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))


import types

def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)


isinstance([1, 2, 3], (list, tuple))
isinstance((1, 2, 3), (list, tuple))


# 获得一个对象的所有属性和方法
print(dir('ABC'))


class MyObject:

    # 类属性
    name = ''
    # 私有属性
    __aa = ''

    def __init__(self):
        # 实例属性
        self.x = 9

    def power(self):
        return self.x * self.x

    def change(self, name):
        self.name = name

    # 不能访问实例属性, 参数必须传入cls
    @classmethod
    def change1(cls, name):
        cls.name = name

    # 不能访问实例属性, 参数不能传入self
    @staticmethod
    def change2(name):
        MyObject.name = name

obj = MyObject()
print(dir(MyObject))
print(dir())


# 测试该对象的属性
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(getattr(obj, 'z', 404))   # 默认值
# delattr(obj,'y')


print(hasattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn)
print(fn())
print(getattr(obj, 'power1', 500))


print('--------实例属性和类属性-------')
class Student():
    name = 'Student'


s = Student()
print(s.name)  # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name)

s.name = 'Michel'  # 这里赋值的是实例属性
print(s.name)
print(Student.name)

Student.name = 'Jack'
print(s.name)
print(Student.name)

del s.name  # 如果删除实例的name属性
print(s.name)  # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了


print('----------测试----------')
class T1():
    # 初始化
    def __init__(self):
        print('init')

    # 创建对象时调用的方法
    def __new__(cls, *args, **kwargs):
        print('new')
        return object.__new__(cls, *args, **kwargs)

    # 析构函数
    def __del__(self):
        print('del')

    # 自定义len函数
    def __len__(self):
        return 10

t1 = T1()
print(len(t1))
