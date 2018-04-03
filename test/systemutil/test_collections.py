# collections | collections是Python内建的一个集合模块，提供了许多有用的集合类。


# namedtuple | namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)


# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。

# 可以验证创建的Point对象是tuple的一种子类
print(isinstance(p, Point))
print(isinstance(p, tuple))


# 类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])


# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈

from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')  # 添加到尾部
q.appendleft('y')  # 添加到首部
print(q)

q = deque(['a', 'b', 'c'])
q.pop()  # 删除最后一个元素
q.popleft()  # 删除第一个元素
print(q)


# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict

from collections import defaultdict
dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])  # key2不存在，返回默认值
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。


# OrderedDict | 有序的Dict
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)  # 无序
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)  # OrderedDict的Key会按照插入的顺序排列

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
from collections import OrderedDict
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0  # 条件运算符，类似java中的 x = true ? 1 : 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

luod = LastUpdatedOrderedDict(3)  # 最大容量3
luod['z'] = 1  # 将被删除掉
luod['y'] = 2
luod['x'] = 3
luod['a'] = 3
print(luod)


# Counter | 计数器 | Counter实际上也是dict的一个子类
# 统计字符出现的个数
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch]+=1
print(c)

