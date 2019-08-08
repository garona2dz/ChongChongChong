from enum import Enum


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


a = 1

print(VIP(a))  # 枚举转换，将取得的值转换成枚举类型
