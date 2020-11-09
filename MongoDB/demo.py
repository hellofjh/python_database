import datetime
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
print(_col_ids)

# 查找单个集合
info = _col.find_one()
info_2 = _col.find_one({'author': 'Mike'}) #带条件
pprint.pprint(info)

# 查找全部集合
infoAll = _col.find()
infoAll_2 = _col.find({'_id': _col_id}) #带条件

# 修改数据
where = {'author': 'Mike'}
update = {'$set': {'author': 'Mike_2'}}
_col.update_one(where, update)
_col.update_many(where, update)

# 删除数据
where = {'author': 'Mike'}
_col.delete_one(where) #删除条件单条数据
_col.delete_many(where) #删除条件多条数据
_col.delete_many({}) #删除所有数据
_col.drop() #删除集合

# 统计数量
count = _col.count_documents({}) #花括号条件为空

# 排序
sort = _col.find({}).sort('author')

# 索引 pymongo.ASCENDING
'''
    索引 
    pymongo.ASCENDING : 1
    pymongo.DESCENDING : -1
    索引对排序的规则：
    1、单键索引：排序规则可以是任意方向
    2、复合索引：所有的键必须'全部相同'与'全部不相同'
'''
_col.create_index([("a", pymongo.DESCENDING)])
_col.create_indexes({'a': pymongo.ASCENDING, 'b': pymongo.DESCENDING})
_col.drop_index('a')
#https://blog.csdn.net/jerryJavaCoding/article/details/82317840

