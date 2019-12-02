# 导入requests
import requests
from dbtools import query

url = "http://132.232.44.158:8080/morning/getAllGoods"

# requests的get方法
# 1. 造请求
res = requests.get(url)
# print(res.text)     # .text所有的响应值

# 2. 判断http状态码 res.status_code
assert res.status_code == 200

# 3. 判断接口返回的信息；获取到success，判断是不是true
a = res.json()
assert a["success"] == True

# 4. 连接查询数据库（可选）
sql = "select * from tb_goods"
b = query(sql)
print(b)
assert len(b) != 0


print("接口测试通过了！")