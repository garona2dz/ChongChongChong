import re
string = "AB8GSAD24324ASD"

def convert(value):
    match = value.group()
    if int(match) >= 5:
        return "#"
    else:
        return "@"

r = re.sub("\d", convert, string)
r1 = re.match("\d", string)  # 从字符串第一个字符开始匹配，返回对象
r2 = re.search("\d", string)  # 整个字符串搜索，返回对象

print(r)
print(r1)
print(r2)
