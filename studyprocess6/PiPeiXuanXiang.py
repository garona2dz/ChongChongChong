import re
la = "PhotonC#JavaC#PHPC#"

def con(value):
    print(value)
    matched = value.group()  #从正则表达式中获取整个字符串，group表示分组
    return "!" + matched + "!"  # 可以将字符串传入函数来操作判断


r1 = re.findall("c#",la)
r2 = re.findall("c#.{1}",la, re.I)  # re.I大小写
r3 = re.findall("c#.{1}",la, re.I | re.S)  # 让 . 能匹配\n ( . 表示匹配除\n外所有字符)
r4 = re.sub("C#","GO",la,0)  # 匹配后替换字符串，0表示可以替换次数
r5 = re.sub("C#","GO",la,1)  # 1表示只能替换一次

r6 = re.sub("C#",con,la)  # 可以把函数传入sub，将匹配的字符串传入函数

la.replace("C#", "GO")  # replace表示替换，调用方法后字符串本身不能改变
la1 = la.replace("C#", "GO")  # 只能赋给新的变量
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(la1)
print(r6)