import re

s = 'life is short, i use python, i love py1thon'
r1 = re.search('(life.*python)', s)
r2 = re.search('life (.*) pyt(.*)1', s)  # 贪婪匹配
r3 = re.findall('life(.*) python', s)
r4 = re.search('life(.*)python, (.*)py', s)

print(r1)  # r1为search返回的对象
print(r1.group())  # 取整个字符串

print(r2.group(1))  # 取第一个括号内的组的匹配的字符串
print(r2.groups())  # 返回所有括号分组内匹配的，元组类型
print(r2.group())   # 返回整个匹配结果和括号没关系，等于group(0)

print(r3)  # r3为findall返回的字符串

print(r4.group(2))
print(r4.group(1, 0, 2))
print(r4.groups())