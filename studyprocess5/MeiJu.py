from enum import Enum


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


for v in VIP:
    print(v)

result1 = VIP.YELLOW == VIP.BLACK  # 枚举间可以比较，但只能等于比较
# 还可以做is身份比较
# 但是不同枚举类之间不能比较
result2 = VIP.YELLOW == 1  # 枚举值比较不正确
print(result1)
print(result2)

print(VIP.BLACK)
print(VIP['BLACK'])
print(VIP.BLACK.name)
print(type(VIP.BLACK))  # 枚举类型
print(type(VIP.BLACK.name))  # 字符串

print(VIP.BLACK.value)  # 打印标签