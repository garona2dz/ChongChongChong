name_list=[{"name":"dezhi","age":18},{"name":"dazhi","age":20}]
find_name=input("请输入要查询的人名：")
#find_age=int(input("请输入要查询的年龄："))

for sth in name_list:
    #print(sth)
    if  sth["name"]==find_name:
        print("%s最帅啦,只有%d岁" %(find_name,sth["age"]))
        break
else:
    print("没有此人!")
print("查找结束!")