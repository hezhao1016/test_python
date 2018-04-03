# 继承和多态


class Animal(object):

    age = 18

    def __init__(self, name):
        self.name = name

    def eat(self):
        print('动物在吃东西...')


class Dog(Animal):

    color = 'black'

    def eat(self):
        print('小狗在吃骨头...')

    def play(self):
        print('小狗在玩棒球...')


class Cat(Animal):

    def eat(self):
        print('小猫在吃鱼...')

    def catchMice(self):
        print('小猫在抓老鼠...')


animal = Animal('动物')
animal.eat()

dog = Dog('旺财')
dog.eat()
dog.play()

cat = Cat('猫咪')
cat.eat()
cat.catchMice()

# 子类可以替代父类 父类不可以替代子类
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(cat, Animal))
print(isinstance(animal, Dog))

print('--------------')
print(animal.name)
print(animal.age)
print(dog.name)
print(dog.age)
print(dog.color)


print('------------------')
def run_twice(animal):
    animal.eat()

run_twice(Animal(''))
run_twice(Dog(''))
run_twice(Cat(''))


# 鸭子类型
# - 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# - 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
# - 动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

class People(object):
    def eat(self):
        print('人饿了要吃肯德基...')

run_twice(People())


# python中没有函数重载，只要使用默认参数、可变参数可以实现类似的效果了


