import pymongo
import pprint

client = pymongo.MongoClient(host='localhost', port=27017) #建立连接池

# 创建数据库与集合后，需要在集合插入数据，数据库与集合才会真正创建
_db = client['test_database'] #创建数据库
_col = _db['test_collection'] #创建集合

data = {
    "author": "Mike",
    "tags": ["mongodb", "python", "pymongo"],
}
# 此处插入一条数据，打印结果数据库与集合都创建了
insert = _col.insert_one(data)
_col_id = insert.inserted_id
print(client.list_database_names()) # 结果：['test_database']
print(_db.list_collection_names()) # 结果：['test_collection']

print(insert)

# 批量插入数据
many_data = [
    {
        "author": "Mike",
        "tags": ["mongodb", "python", "pymongo"],
    },
    {
        "author": "Eliot",
        "tags": ["java", "docker", "Spring"],
    }
]
insert_many = _col.insert_many(many_data)
_col_ids = insert_many.inserted_ids
print(insert_many)