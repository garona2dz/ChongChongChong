from enum import Enum


class VIP(Enum):
    YELLOW = 1
    GREEN = 1  # 枚举中数值相同，则后面的是前面的别名
    BLACK = 3
    RED = 4


for v in VIP:
    print(v)

for v in VIP.__members__:
    print(v)

for v in VIP.__members__.items():
    print(v)

print(VIP.GREEN)