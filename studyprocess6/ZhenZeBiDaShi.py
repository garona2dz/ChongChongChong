import re
string1 = "ssssPPuSdzasfsdnfasn"
string2 = "python 23java332php"
string3 = "pytho0python1pythonn2"

print(string1.index("dz") > -1)  # index方法返回字符串所在索引，没有也不会报错
print("dz" in string1)

r1 = re.findall("[a-z]{3,6}",string2)  # 贪婪匹配，严格匹配
r2 = re.findall("[a-z]{3,6}?",string2)  # 非贪婪匹配，严格匹配
r3 = re.findall("python?",string3)  # ?:前面字符匹配0次或一次

print(r1)
print(r2)
print(r3)
