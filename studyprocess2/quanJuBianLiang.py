num = 9
num1 = 19
list1 = [1, 2]
list2 = [3, 4]
list3 = [45, 54]


def fun1(num1):
    num = 6  # 新建内存空间，并指向它,且都被看作局部变量
    print(num)
    num1 = 91
    print(num1)


def fun2():
    list1 = [5, 6]  # = 赋值就等于新建内存空间，并指向它，且被看成局部变量
    print(list1)
    list2.append(999)  # 使用方法，没有新建内存空间，还是原来的地址，通过方法来操作
    print(list2)


def fun3(list1,list2,list3):
    print(list1)
    list1 = [7,8]    # 在函数内部，先赋值就重新引用另一个内存空间，函数内局部变量
    print(list1)
    list1.append(666)
    print(list1)
    list1[2] = 333   # 前面函数里已经新建内存空间了，不会再改变引用，直接修改
    print(list1)

    print(list3)
    list3[1] = 444   # 等号左边可以看出不是在定义，是在给已定好的变量重新赋值，函数里没有定义该变量，
    print(list3)     # 就自动向前寻找，这种赋值方式不会改变引用，还是原来的内存地址，所以能修改

    print(list2)
    list2.append(777)  # 使用方法改变则不会改变引用
    print(list2)

fun1(num1)
print(num)  # 外界变量
print(num1)  #外界变量，不受函数里局部变量影响

fun2()
print(list1)  # 外界变量，不受函数理新建的局部变量影响
print(list2)  # 直接调用方法操作原来地址变量

fun3(list1, list2, list3)
print(list1)  # 外界变量，不受函数理新建的局部变量影响
print(list2)  # 可变型参数可以在函数内部直接调用方法来操作
print(list3)  # 可变型参数切片取值，说明是已经定义好的，再赋值等于不改变引用，所以可以改变外界参数