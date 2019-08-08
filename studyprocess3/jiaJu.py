class HouseItem:
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        return "%s占地:%.2f" %(self.name,self.area)

class House:
    def __init__(self,house_type,area):
        self.house_type=house_type
        self.area=area
        self.free_area=area
        self.house_item=[]

    def __str__(self):
        return ("\n户型：%s \n总面积：%.2f 剩余面积：%.2f\n家具列表：%s" %(self.house_type,
                                           self.area,self.free_area,self.house_item))

    def add_item(self,item):
       # item_area+=1
        print("添加的家具是：%s 占地是：%s"%(item.name,item.area))
        if item.area>=self.free_area:
            print("%s家具面积太大，摆放不下！"%(item.name))
            return
        self.house_item.append(item.name)
        self.free_area-=item.area
        print("添加家具成功！")


bed=HouseItem("床",35)
table=HouseItem("桌子",2.2)
house1=House("大床房",24.3)

house1.add_item(bed)
house1.add_item(table)

#print(bed)
#print(table)
print(house1)
