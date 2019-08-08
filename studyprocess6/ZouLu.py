# x = 3, 5, 2
# f(x) = 3, 8, 10

# result = 0
# def f(x):
#     result = result + x   #  此处会报错，说result没定义，因为在等号左边result被看成局部变量来使用
#     return result         #  但是没定义，所以报错。如果result不出现在等号左边，函数在定义时发现result
                            #  没有定义，会自动向函数上面搜索result的定义。

origin = 0

def go(step):
    global origin   # 使用全局变量来记录每次结果
    new_pos = origin + step
    origin = new_pos
    print(new_pos)

go(2)
go(3)
go(5)
print("-------")

position = 0
def fun1(pos):
    def fun2(step):
        nonlocal pos    # nonlocal直接声明不是局部变量 
        new_pos = pos + step
        pos = new_pos
        return pos
    return fun2

person = fun1(position)
print(person(2))
print(person.__closure__[0].cell_contents)  #闭包
print(position)  # 并没利用global来改变外界变量，使函数更加封闭
print(person(3))
print(position)
print(person(5))










