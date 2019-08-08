class Cat:
    name = "tom"

    def __init__(self):
        self.name1 = "dezhi"

    def eat(self):
        print("吃！")

    def drink(self):
        print("喝！")


Tom = Cat()
Tom.eat()
Tom.drink()

print(Cat.name)
# print(Cat.name1)  # 类不能访问对象属性
print(Tom.name)  # 对象可以访问类属性
print(Tom.name1)  # 对象可以访问对象属性

print(id(Cat.name))
print(id(Tom.name))  # 都引用相同的类属性，所以内存中位置相同
print(id(Tom.name1))
Tom.name = "Tom"  # 利用对象名修改类属性会自己创建个对象属性和类属性同名，再次访问时就访问对象属性
Tom.name1 = "de"
print(Tom.name)
print(Cat.name)
print(id(Cat.name))
print(id(Tom.name))  # 此时已经不再引用相同，一个类属性，一个对象属性
print(id(Tom.name1))  # 赋值后内存地址会改变
print(Tom) # 打印对象的类名和对象在内存中的地址
print("%x %d" % (id(Tom),id(Tom)))
print(id(Tom))
