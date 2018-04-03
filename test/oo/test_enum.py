# 枚举类

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.Jan)

# 列举所有成员

for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)


from enum import Enum,unique

@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print('------------------')
day1 = Weekday.Mon
print(day1)
print(Weekday['Sun'])
print(Weekday.Sat.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Fri)
print(Weekday(1))
print(day1 == Weekday(1))
print('----------------')


@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if isinstance(value, Gender):
            self._gender = value
        else:
            raise TypeError('Gender类型输入错误')

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
print(bart.gender)
bart.gender = Gender.Female
print(bart.gender)

