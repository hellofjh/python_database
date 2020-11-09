from Mysql.config import con
from Mysql.config import pool

cursor = con.cursor() #游标，用于执行sql语句

create_table_sql = "CREATE TABLE `browser` (" \
                   "`id` INT AUTO_INCREMENT PRIMARY KEY COMMENT 'id', " \
                   "`name` VARCHAR(128) COMMENT '名字', " \
                   "`url` VARCHAR(255) COMMENT '官网'" \
                   ")"
# cursor.execute(create_table_sql)

_index1 = "ALTER TABLE `browser` ADD UNIQUE INDEX name(name)" #唯一索引
_index2 = "CREATE INDEX url ON `browser`(url)" #普通索引
# for sql in [_index1, _index2]:
    # cursor.execute(sql)

insert_sql = "INSERT INTO `browser`(name, url) VALUES (%s, %s)"
values = ('Chrome', "http://www.google.cn/chrome/")
# cursor.execute(insert_sql, values) #插入单条数据
# con.commit()

values = [
    ('Chrome', "http://www.google.cn/chrome/"),
    ('Firefox', "http://www.firefox.com/"),
    ('Safari2', "https://www.apple.com.cn/safari/")
]
# cursor.executemany(insert_sql, values) #插入多条数据
# con.commit()

name = '1 OR 1=1'
url = '1 OR 1=1'
select_sql = "SELECT * FROM `browser` WHERE `name`=%s and `url`=%s"
cursor.execute(select_sql, (name, url))
# print(cursor.fetchone()) #获取单条数据
print(cursor.fetchall()) #获取全部数据
# for info in cursor.fetchall():
#     print(info)

update_sql = "UPDATE `browser` SET `url`='http://www.firefox.com.cn' WHERE `name`='Firefox';"
# cursor.execute(update_sql)
# con.commit()

# delete_sql = "DELETE FROM `browser` WHERE `name` = 'Firefox';"
# cursor.execute(delete_sql)
# con.commit()

# 异常处理与事务控制


# cursor.execute(delete_sql, ['Safari1'])
try:
    con.start_transaction()
    cursor = con.cursor()
    delete_sql = "DELETE FROM `browser` WHERE `name` = %s"
    cursor.execute(delete_sql, ['Firefox'])
except Exception as e:
    con.rollback() #回滚
else:
    con.commit() #提交