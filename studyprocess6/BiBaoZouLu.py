result = 0


def step(x):
    # nonlocal result
    global result  # 全局变量保存值，代码尽量少用全局变量
    result += x
    return result


print(step(2))
print(step(3))
print(step(5))


def b_step(pos):  # 闭包保存上次调用状态
    def go(num):
        nonlocal pos  # 声明不是局部变量
        pos += num
        return pos
    return go


f = b_step(0)
print(f(2))
print(f(3))