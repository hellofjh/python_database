from Redis.connect import _redis

# str
'''
    set(name, value, ex=None, px=None, nx=False, xx=False)
    ex: 过期秒
    px: 过期毫秒
    nx: 设置为True，只有name不存在才执行
    xx: 设置为True，只有name存在才执行
'''
_redis.set('python', 'test', ex=3) #设置值
_redis.get('python') #获取值 结果：test

_redis.mset({
    'database': 'redis',
    'method': 'mset'
}) #批量设置值
_redis.mget('database', 'method') #批量获取值 结果：redis, mset
_redis.strlen('database') #获取对应值长度 结果：5

'''
    incr/decr(name, amount=1)
    name: 自增/自减对应值，没有则创建
    amount: 自增/自减数-整数
    常见应用场景：点赞数
'''
_redis.incr('test:incr', 2) #自增2
_redis.decr('test:incr', 1000) #自减1000

_redis.exists('database') #判断是否存在 结果：Ture
_redis.append('database', '2.0') #对应的值后面追加内容
_redis.delete('database')  #删除
_redis.keys() #获取全部键名


# hash
_redis.hset('hash', 'key:', 'value') #创建键值对 没有就新增，有的话就修改
_redis.hget('hash', 'key:')  #单个取hash的key对应的值

_redis.hmset('hash2', {'key2:':'value2', 'key3:':'value3'}) #批量创建键值对
_redis.hmget('hash2', ['key2:', 'key3:']) #批量获取键值对
_redis.hkeys('hash2') #获取所有的键名
_redis.hvals('hash2') #获取所有的键值
_redis.hgetall('hash2') #获取所有的键名对应键值

_redis.hlen('hash2') #获取对应长度

'''
    hincrby(name, key, amount=1)
    name: redis中的name
    key: hash对应的key
    amount: 自增/自减数-整数
'''
_redis.hincrby('test_hincr', 'num', 1) #自增name对应的hash中的指定key的值

_redis.hexists('hash2', 'key2') #判断name对应key的值是否存在
_redis.hdel('hash2', 'key2') #删除键值对


# list
_redis.lpush('list', 4, 3, 2, 1) #在name对应的list中从最左边添加元素，没有则创建并添加
_redis.lpushx('list2', 10) #在name对应的list中从最左边添加元素，没有则不进行
_redis.rpush('list', 5, 6, 7, 8)  #在name对应的list中从最右边添加元素，没有则创建并添加
_redis.rpushx('list2', 10) #在name对应的list中从最右边添加元素，没有则不进行
_redis.llen('list') #列表长度

'''
    linsert(name, where, refvalue, value)
    name - redis的name
    where - BEFORE或AFTER
    refvalue - 标杆值，即：在它前后插入数据
    value - 要插入的数据
'''
_redis.linsert('list', 'after', '9', 10) #新增（固定索引号位置插入元素）

'''
    r.lset(name, index, value)
    name - redis的name
    index - list的索引位置
    value - 要设置的值
'''
_redis.lset('list', '9', 9) #修改（指定索引号进行修改）

'''
    name - redis的name
    value - 要删除的值
    num - 0：删除列表中所有指定值； 2：从前到后，删除2个； -2：从后到前，删除2个
'''
_redis.lrem('list', '9', 1) #删除（指定值进行删除）

_redis.lpop('list') #列表最左边删除并返回
_redis.rpop('list') #列表最右边删除并返回

_redis.lindex('test', 0) #在name对应的列表中根据索引获取列表元素


# set 无序
_redis.sadd('set', 1, 2, 3, 4) #对应的集合中添加元素
_redis.scard('set') #集合长度
_redis.smembers('set') #获取集合中所有的成员

_redis.sdiff('set1', 'set2') #差集
_redis.sdiffstore('set3', 'set1', 'set2') #找到两集合的差集存储到新的集合

_redis.sinter("set1", "set2") #交集
_redis.sinterstore('set3', 'set1', 'set2') #找到两交集的差集存储到新的交集

_redis.sunion("set1", "set2") #并集
_redis.sunionstore('set3', 'set1', 'set2') #找到两并集的差集存储到新的并集

_redis.sismember('set', 10) #值是否集合成员

_redis.spop('set') #随机删除集合一个成员
_redis.srem('set', 10) #删除集合指定成员


# set 有序
_redis.zadd('zset', {'z1':1, 'z2':2, 'z3':3}) #新增有序集合
_redis.zscore('zset', 'z1') #获取分数 已排序
_redis.zcard('zset') #集合长度
_redis.zcount('zset', 1, 2) #获取name对应的有序集合中分数

'''
    zrevrange(name, start, end, withscores=False, score_cast_func=float) #获取可排序集合元素
    name - redis的name
    start - 有序集合索引起始位置（非分数）
    end - 有序集合索引结束位置（非分数）
    desc - 排序规则，默认按照分数从小到大排序
    withscores - 是否获取元素的分数，默认只获取元素的值
    score_cast_func - 对分数进行数据转换的函数
'''

_redis.zrevrange("zset1", 0, -1, withscores=True) #获取有序集合中所有元素和分数,分数倒序

_redis.zrevrangebyscore('zset2', 30, 10, withscores=True) #根据分数范围获取有序集合的元素并排序

_redis.zcount('zset2', 1, 10) #区间和

_redis.zincrby("zset2", "z1", amount=2)  # 每次将z1的分数自增2

_redis.zrem('zset2', 'z1') #删除单个
_redis.zremrangebyrank('zset2', 1, 10) #根据排行范围删除
_redis.zremrangebyscore('zset2', 1, 10) #根据分数范围删除


