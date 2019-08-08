import json

# json object array
# 在python中转成列表
# 反序列化  json对象 转换成 python 的数据格式
# 序列化    python数据类型转换成 json
json_str = '[{"name": "dezhi", "age":18}, {"name": "guoguo", "age":23}]'

student = json.loads(json_str)
print(type(student))
print(student)

 