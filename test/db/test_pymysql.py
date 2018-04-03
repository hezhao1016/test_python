# pymsql是Python中操作MySQL的模块，其使用方法和MySQLdb几乎相同。但目前pymysql支持python3.x而后者不支持3.x版本。

# 安装MySQL驱动
# pip install pymysq


# 执行SQL

import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, db='test', user='root', passwd='root', charset='utf8')
# 注意：存在中文的时候，连接需要添加charset='utf8'，否则中文显示乱码。
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from book")

# 获取剩余结果的第一行数据
# row_1 = cursor.fetchone()
# print(row_1)
# 获取剩余结果前n行数据
# row_2 = cursor.fetchmany(3)
# print(row_2)
# 获取剩余结果所有数据
row_3 = cursor.fetchall()
print(row_3)

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update book set name = '追风筝的人' where id = %s", (1,))

# 执行SQL，并返回受影响行数,执行多次
# effect_row = cursor.executemany("insert into book(id,name,stu_id) values(%s,%s,%s)", [(None, "梦回唐朝", "1"), (None, "看不见的风景", "1")])

#获取自增id
# new_id = cursor.lastrowid

# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()

# 移动游标
# 注：在fetch数据时按照顺序进行，可以使用cursor.scroll(num, mode)来移动游标位置，如：
# cursor.scroll(1, mode='relative')  # 相对当前位置移动
# cursor.scroll(2, mode='absolute')  # 相对绝对位置移动



# 使用with简化连接过程

import pymysql
import contextlib

# 定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def mysql(host='127.0.0.1', port=3306, db='test', user='root', passwd='root', charset='utf8'):
    conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
    # 默认元祖类型,游标设置为字典类型
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()


# 执行sql
with mysql() as cursor:
    print(cursor)
    row_count = cursor.execute("select * from book")
    row_1 = cursor.fetchone()
    print(row_count, row_1)
    print(row_1['name'])


