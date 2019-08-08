import math


def reverse(x):  # 此方法是用余数，还可以直接字符串逆序str[::-1]
    result = 0
    yu_list = []
    x_in = abs(x)
    while True:
        yu = x_in % 10
        yu_list.append(yu)
        shang = math.floor(x_in / 10)
        x_in = shang
        if shang == 0:
            break

    for i in yu_list:
        result = result * 10 + i

    if result in range(-(2**31), 2**31 - 1):
        print(result if x >= 0 else - result)
    else:
        print(0)


reverse(-4346234)
