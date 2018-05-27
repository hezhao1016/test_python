# 使用MySQL

# 安装MySQL驱动
# 由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。MySQL官方提供了mysql-connector-python驱动，但是安装的时候需要给pip命令加上参数--allow-external：
# $ pip install mysql-connector-python --allow-external mysql-connector-python
# 如果上面的命令安装失败，可以试试另一个驱动：
# $ pip install mysql-connector


import mysql.connector
import pprint

conn = mysql.connector.connect(host='127.0.0.1', port='3306', database='test', user='root', password='root')

cursor = conn.cursor()

# 创建user表
cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")

# 插入一行记录，注意MySQL的占位符是%s
cursor.execute("insert into user (id, name) values (%s, %s)", ['1', 'Michael'])
count = cursor.rowcount
print(count)

# 提交事务
conn.commit()
cursor.close()

# 运行查询
cursor = conn.cursor()
cursor.execute("select * from user where id = %s", ('1',))
values = cursor.fetchall()
pprint.pprint(values)

# 关闭Cursor和Connection
cursor.close()
conn.close()



# 由于Python的DB-API定义都是通用的，所以，操作MySQL的数据库代码和SQLite类似。
# 小结
    # 执行INSERT等操作后要调用commit()提交事务；
    # MySQL的SQL占位符是%s。
