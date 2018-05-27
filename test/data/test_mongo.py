# 使用Python操作MongoDB
# 安装驱动：pip install pymongo

from pymongo import MongoClient
import datetime
import pprint

# 创建MongoClient,使用默认主机、接口
# client = MongoClient()
# 指定主机和端口
# client = MongoClient('127.0.0.1', 21017)
# 使用MongoDB URI格式
client = MongoClient('mongodb://localhost:27017/')

# 获取数据库
# db = client.test
db = client['test']

# 获取集合
# collection = db.blog
collection = db['blog']

# 列出数据库中的所有集合
cur_collection = db.collection_names(include_system_collections=False)
print('-----------列出数据库中的所有集合-----------')
print("cur_collection is :", cur_collection)
print('---------------------------------')

# 插入单个文档
"""
blog = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}
inserted_id = collection.insert_one(blog).inserted_id
print("插入后的主键是：%s" %inserted_id)
"""

# 插入多个文档
"""
new_blogs = [{"_id": 1000,
               "author": "Curry",
               "text": "Another post!",
               "tags": ["bulk", "insert"],
               "date": datetime.datetime(2017, 11, 12, 11, 14)},
              {"_id": 1001,"author": "Maxsu",
               "title": "MongoDB is fun",
               "text": "and pretty easy too!",
               "date": datetime.datetime(2019, 11, 10, 10, 45)}]
result = collection.insert_many(new_blogs)
print("批量插入后的主键是:", result.inserted_ids)
"""

# 获取文档
# document = collection.find_one()
document = collection.find_one({"author": "Curry"})
print('-----------获取单个文档-----------')
pprint.pprint(document)
print('---------------------------------')

list = collection.find({})
print('-----------获取多个文档-----------')
for doc in list:
    pprint.pprint(doc)
print('---------------------------------')

# count
print("posts count is = ", collection.count())
print("posts's author is Maxsu count is =", collection.find({"author": "Maxsu"}).count())


# 修改文档
result = collection.update_many({"author": "Maxsu"}, {"$set": {"text": "哈哈哈！"}})
print("修改影响行数:", result.modified_count)

# 删除文档
result = collection.delete_many({"author": "Curry"})
print("删除影响行数:", result.deleted_count)