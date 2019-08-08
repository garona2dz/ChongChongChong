class Gun:
    def __init__(self, model, bullet):
        self.model = model
        self.bullet_max_number = bullet
        self.bullet_count = 0

    def __str__(self):
        return print("枪名：%s 最大填弹数量：%s") % (self.model, self.bullet_max_number)

    def add_bullet(self):
        bullet_number = int(input("装弹数目："))
        if (bullet_number + self.bullet_count) > self.bullet_max_number:
            print("装弹超过最大容量！自动装满%s发子弹！" % self.bullet_max_number)
            self.bullet_count = self.bullet_max_number
        else:
            self.bullet_count += bullet_number
            # if self.bullet_count >= self.bullet_max_number:
            print("装填子弹%d发成功！" % bullet_number)
        return

    def shoot(self, times=1):
        if self.bullet_count <= 0:
            print("没有子弹，请装弹！")
            self.add_bullet()
        if times > self.bullet_count:
            print("射击次数大于剩余子弹数量，自动射完所有子弹！")
            self.bullet_count = 0
            print("子弹数量为0，继续射击请装弹！")
        else:
            print("突"*times)
            print("射击成功%s次！" % times)
            self.bullet_count -= times
            print("还有%s颗子弹！" % self.bullet_count)
        return


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None  # 一个对象的属性可以是另一个对象

    def __str__(self):
        return print("士兵：%s" % self.name)

    def fire(self):
        if self.gun is None:
            print("士兵%s还没枪，无法开火！" % self.name)
        else:
            fire_times = int(input("开火次数："))
            """
            if self.gun.bullet_count<=0:
                print("没有子弹，请装弹！")
                bullet_number=int(input("装弹数目："))
                self.gun.add_bullet(bullet_number)
            """
            self.gun.shoot(fire_times)
            # print("准备开火！")
            # print("突突突%d次！" % fire_times)


AK47 = Gun("AK47", 10)
# print(Gun.__mro__) 从类中调用方法顺序，从左往右，没有就报错
print(dir(object))
dezhi = Soldier("dezhi")
dezhi.gun = AK47
dezhi.fire()




