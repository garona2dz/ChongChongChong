from enum import Enum
from enum import IntEnum, unique


class VIP(Enum):
    YELLOW = 'yellow'
    GREEN = 2
    BLACK = 3
    RED = 4


@unique  # 保证枚举类中标签的值是唯一的
class VIP1(IntEnum):  # IntEnum表示标签值只能int数值
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


print(VIP.YELLOW.value)
print(VIP1.YELLOW.value)
print(VIP.YELLOW.name)
print(VIP1.YELLOW.name)