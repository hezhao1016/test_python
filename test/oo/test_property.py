# 使用property

class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(60) # ok!
print(s.get_score())
# s.set_score(9999)




class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    #只读属性
    @property
    def age(self):
        return 2018 - self._birth
        
s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
print(s.score) # OK，实际转化为s.get_score()
# s.score = 9999
s.birth = 1996
print('%s 岁' %s.age)





# property 未赋值前不能调用，报AttributeError异常


# 判断属性是否存在
# hasattr(object, name)
#    说明：判断对象object是否包含名为name的特性（hasattr是通过调用getattr(ojbect, name)是否抛出异常来实现的）。
#    参数object：对象。
#    参数name：特性名称。
#    返回为True或者为False

# 自己也可以定义一个方法

# def  getattribute(self, name):
#    try:
#         r = object.__getattribute__(self, name)
#    except:
#         r = None
#    return r


# 做成一个工具类
class AttrUtil(object):
    # @staticmethod
    # def getattribute(self, name):
    #     try:
    #         r = object.__getattribute__(self, name)
    #     except:
    #         r = None
    #     return r

    @staticmethod
    def getattribute(self, name):
        return getattr(self, name, None)


print(AttrUtil.getattribute(s,'birth1'))



# import calendar
# cal = calendar.month(2016, 1)
# print("以下输出2016年1月份的日历:")
# print(cal)