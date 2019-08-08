import re
qq = "123456789"
string1 = "pythonpythonpythonpythonpythonpython"
string2 = "wwww"

r = re.findall("\d{4, 8}", qq)
r1 = re.findall("^\d{4,8}$",qq)  # 边界匹配，匹配完整字符串，^表示必须从开始匹配，$表示从结尾匹配
r2 = re.findall("(python){3}",string1)  # ()中是且关系
r3 = re.findall("[www]{3}",string2)   # []中是或关系

print(r)
print(r1)
print(r2)
print(r3)

