import json

# JSON Object
json_str = '{"name": "dezhi", "age":18}'  # 在JavaScript中是对象，在python中转成字典
# json 中的引号必须为双引号
student = json.loads(json_str)

print(type(student))
print(student)
print(student['age'])