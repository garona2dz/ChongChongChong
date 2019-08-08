import json

student = [
    {'name': 'dezhi', 'age': 18},
    {'name': 'guoguo', 'age': 23}
]
# 序列化
json_str = json.dumps(student)

print(type(json_str))
print(json_str)