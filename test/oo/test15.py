# 多重继承
'''
                ┌───────────────┐
                │    Animal     │
                └───────────────┘
                        │
           ┌────────────┴────────────┐
           │                         │
           ▼                         ▼
    ┌─────────────┐           ┌─────────────┐
    │   Mammal    │           │    Bird     │
    └─────────────┘           └─────────────┘
           │                         │
     ┌─────┴──────┐            ┌─────┴──────┐
     │            │            │            │
     ▼            ▼            ▼            ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│   Dog   │  │   Bat   │  │ Parrot  │  │ Ostrich │
└─────────┘  └─────────┘  └─────────┘  └─────────┘
'''



# 动物
class Animal(object):
    def __init__(self, name):
        self.__name = name

    def sayHello(self):
        print('My Name is %s' % self.__name)

# 哺乳动物类
class Mammal(Animal):
    def __init__(self, name, foot):
        super(Mammal, self).__init__(name)
        self.__foot = foot

    def sayFoot(self):
        print('我有 %s 只脚' % self.__foot)

# 鸟类
class Bird(Animal):
    def __init__(self, name, color):
        super(Mammal, self).__init__(name)
        self.__color = color

    def sayColor(self):
        print('我的羽毛是 %s 色' % self.__color)

# 跑的能力
class RunnableMixIn(object):
    def run(self):
        print('Running...')

#飞的能力
class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

# 肉食行为
class CarnivorousMixIn(object):
    def eat(self):
        print('吃肉...')

# 植食行为
class HerbivoresMixIn(object):
    def eat(self):
        print('吃草...')

# 狗
class Dog(Mammal, RunnableMixIn,CarnivorousMixIn):
    pass

#蝙蝠
class Bat(Mammal, FlyableMixIn,CarnivorousMixIn):
    pass

#鹦鹉
class Parrot(Bird, FlyableMixIn,HerbivoresMixIn):
    pass

#鸵鸟
class Ostrich(Bird, RunnableMixIn,HerbivoresMixIn):
    pass


# MixIn
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。



d = Dog('大黄',4)
d.sayHello()
d.sayFoot()
d.eat()
d.run()





# =================================================以下是接口
class IorderRepository:  ##接口
    def fetch_one_by(self, nid):
        '''
        获取单条数据的方法，所有的继承呢当前类的类必须继承
        :param nid:
        :return:
        '''
        # raise Exception('子类中必须包含该方法')


class OrderReposititory(IorderRepository):  # 类
    def fetch_one_by(self, nid):
        print(nid)


obj = OrderReposititory()
obj.fetch_one_by(1)






# ============================================抽象类抽象方法
import abc

class Foo(metaclass=abc.ABCMeta):  ##抽象类
    def f1(self):
        print(123)

    def f2(self):
        print(456)

    @abc.abstractmethod  ##抽象方法
    def f3(self):
        '''
        ???
        :return:
        '''


class Bar(Foo):
    def f3(self):
        print(33333)


b = Bar()
b.f1()
b.f2()
b.f3()