# 定制类

class Student(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object (name:%s)' % self.name
    __repr__ = __str__

print(Student('Frank'))

# 直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。



class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
for n in f:
    print(n)

print('--------------------')
print(f[5])
print(f[0:5])
print(f[:10])




class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        if attr == 'name':  # 注意，只有在没有找到属性的情况下，才调用__getattr__
            return '张三'
        # 未找到，默认返回None
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


s = Student()
print(s.name)
print(s.score)
print(s.age())
# print(s.xxx)


# 完全动态调用的特性
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    __call__ = __getattr__

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)
print(Chain().users('HeZhao').repos)



print('---------------------')
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
class Student(object):
    def __init__(self, name='无名'):
        self.name = name

    # def __call__(self):
    #     print('My name is %s.' % self.name)

    def __call__(self,arg='name'):
        print('My %s is %s.' % (arg,self.name))


s = Student()
# s()
s("NAME")




# 可以把对象看成函数，把函数看成对象,能被调用的对象就是一个Callable对象
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
print(callable(Student()))
print(callable(max))
print(callable(1))