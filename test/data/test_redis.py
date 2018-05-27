# 使用Python操作Redis
# 安装驱动：pip install redis

import redis

# 严格连接模式,
# StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令
# r = redis.StrictRedis(host="127.0.0.1", port=6379)

# Python化的连接模式
# Redis与StrictRedis的区别是：Redis是StrictRedis的子类，用于向前兼容旧版本的redis-py，并且这个连接方式是更加"python化"的
r = redis.Redis(host="127.0.0.1", port=6379)

# 连接池
# pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
# r = redis.Redis(connection_pool=pool)

###### 字符串
# 存值
r.set('name1', '张三')
r.set('name2', '李四', ex=60)  # 设置60秒过期时间
r.mset(name3='jack', name4='tom')  # 批量设置

# 取值
print(r.get('name1').decode('utf-8'))

###### 哈希
# 存值
r.hset('book', '西游记', '吴承恩')
r.hmset('book', {'红楼梦': '曹雪芹', '水浒传': '施耐庵'})

# 取值
print(r.hget("book", "西游记").decode('utf-8'))
# 批量获取
for x in r.hmget("book", "红楼梦", "水浒传"):
    print('hmget - ', x.decode('utf-8'))
# 所有键值
for x in r.hgetall("book"):
    print('hgetall - ', x.decode('utf-8'))

