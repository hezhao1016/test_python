# 序列化

import pickle

d = dict(name='Bob', age='20', score=80)

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
data = pickle.dumps(d)
f = open('F:/xdir/dumps.txt', 'wb')
f.write(data)
f.close()

# pickle.dump()直接把对象序列化后写入一个file-like Object
with open('F:/xdir/dump.txt', 'wb') as f1:
    pickle.dump(d, f1)


# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象
with open('F:/xdir/dumps.txt', 'rb') as f2:
    data = bytearray()
    while 1:
        buf = f2.read(1024)
        if not buf:
            break
        for x in buf:
            data.append(x)
    d1 = pickle.loads(data)
    print(d1)

# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
with open('F:/xdir/dump.txt', 'rb') as f3:
    d2 = pickle.load(f3)
    print(d2)



# JSON 模块
import json

d = dict(name='Bob', age=20, score=88)

# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object
json_str = json.dumps(d)
print(json_str)

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
d1 = json.loads(json_str)
print(d1)


# 实体类转换成JSON
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def __str__(self):
        return 'Student object (name:%s,age:%s,score:%s)' % (self.name,self.age,self.score)

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)
# 转换函数
print(json.dumps(s, default=student2dict))
# 把任意class的实例变为dic
print(json.dumps(s, default=lambda obj: obj.__dict__))


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))



# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数
# 想输出真正的中文需要指定ensure_ascii=False
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)

#用偏函数，默认支持中文
import functools
mydumps = functools.partial(json.dumps, ensure_ascii=False)
s = mydumps(obj)
print(s)
