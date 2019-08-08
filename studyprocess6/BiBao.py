def f():
    a = 10

    def f1():
        a = 20  # 此时a是个局部变量
        #  print(a)
        print("---")

    print(a)
    print("----")
    f1()
    print(a)
    print("-----")
    return f1

f()  #  输出为 10 20 10 20

def f2():
    a = 10

    def f3():
        a = 20  # 此时a是个局部变量
        print(a)
        print("---")

    print(a)
    print("----")
    f3()
    print(a)
    print("-----")
    return f3

print(f2())
print(f2.__closure__)  # 当a在函数内部被赋值时，a是局部变量，不是环境变量，此时不会构成闭包