class MusicPlayer(object):
    address = None

    def __new__(cls, *args, **kwargs):
        """
        重写__new__方法，定义一个类属性用来存放新建对象是分配的空间地址，
        并将其返回给__init__方法用来初始化，再新建新的对象时，就会调用重写的__new__方法，
        不用再分配新的，直接使用已经存在类属性中的地址引用，所以新建的对象都在一个内存空间中
        """
        if cls.address is None:
            cls.address = super().__new__(cls)
        return cls.address


player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)  # 单例，两个对象的内存空间一样
