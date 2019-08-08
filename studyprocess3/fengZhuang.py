class person:
    def __init__(self,name,weight):
        """初始化定义名字体重
        """
        self.name=name
        self.weight=weight
    def __str__(self):
        return "名字：%s,体重：%s" %(self.name,self.weight)
    def run(self):
        print("名字：%s,跑完步体重：%s" %(self.name,self.weight-1) )
    def eat(self):
        print("名字：%s,吃完体重：%s" % (self.name, self.weight+1))

dezhi=person("dezhi",75)
print(dezhi)
dezhi.run()
dezhi.eat()


