import redis


r = redis.Redis(host="localhost", port=6379, db=1)
# r = redis.Redis(host='localhost', port=6379, db=0)
result = r.set('name', '张三')
print(result)
result = r.get('name')
print(result)
print(r.delete('name'))
r.set('name', 'itcast')
print(r.get("name"))
r.set('name', 'heima')
print(r.get("name"))
print(r.mset({'age':"13", "gender":"man"}))

print(r.keys())