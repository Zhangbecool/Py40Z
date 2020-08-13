import redis


r = redis.Redis(host="localhost", port=6379, db=1)
# r = redis.Redis(host='localhost', port=6379, db=0)
# result = r.set('name', '张三')
# print(result)
# result = r.get('name')
# print(result)
# print(r.delete('name'))
# r.set('name', 'itcast')
# print(r.get("name"))
# r.set('name', 'heima')
# print(r.get("name"))
# print(r.mset({'age':"13", "gender":"man"}))
# print(r.mget("name", "age"))
# r.append('name', 'py40')
# print(r.get('name'))
# r.setex('code',60, 115)
# print(r.ttl('code'))
#
# print(r.keys())

# hash
print('-'* 30)

# r.hset('a1','name','tom')
# r.hmset('a1',{'age':14, 'gender': 'man'})
# print(r.hget('a1', 'name'))
# print(r.hmget('a1', 'age', 'gender'))
# print(r.hkeys('a1'))
# print(r.hvals('a1'))
# print(r.hdel('a1','gender'))
# print(r.hkeys('a1'))
# print(r.hvals('a1'))
# print(r.keys())
# print(r.exists('code'))
#  list
print('-' * 30)

# print(r.lpush('list', 1, 2, 3))
# r.rpush('list', 4)
# print(r.lrange('list', 0, -1))
# linsert 参数 key  位置(before|after) 在那个元素  插入内容 如果元素不存在则返回-1 什么都不做
# r.linsert('list','before', 1, 5)
# r.linsert('list', 'after', 5, 6)
# print(r.linsert('list', 'after', 8, 10))
# r.lset('list', 1, 7)
# print(r.lrange('list', 0, -1))

# set
# print(r.sadd('set', 1))
# print(r.sadd('set', 2))
# print(r.smembers('set'))
# print(r.srem('set', 1))
# print(r.smembers('set'))

# zset

# print(r.zadd('zset', {10:1, 11:2, 9:3}))
# print(r.zadd('zset', {12:3, 13:2, 14:1}))
# r.zadd('zset', {'a':22})
print(r.zrangebyscore('zset', 1, 5))
print(r.zscore('zset', 12))
print(r.zrem('zset', 10))
print(r.zrange('zset', 0, -1))
print(r.zremrangebyscore('zset', 1, 5))
print(r.zrange('zset', 0, -1))

