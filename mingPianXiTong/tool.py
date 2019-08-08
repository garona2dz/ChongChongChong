message_list=[]

def tuiChu():
    print("谢谢使用系统！再见！")
    return

def chaZhao():
    #xingMing=input("请输入要查找的姓名：")
    if message_list==[]:
        print("没有任何名片信息！请先填加!")
        return
        """
        while True:
            print("0.返回上级菜单")
            choice1 = input("请再次选择功能：")
            if choice1 == "0":
                return  # 直接退出函数返回上级菜单
            else:
                print("输入错误，请重新输入!")
        """
    else:
        xingMing = input("请输入要查找的姓名：")
        for i in message_list:
            if xingMing==i["name"]:
                print("-"*60)
                print("姓名\t\t年龄\t\t电话号码")
                print("%s\t\t%s\t\t%s" %(i["name"],i["age"],i["phone_number"]))
                print("-" * 60)
                print("显示完毕！")
                while True:
                    print("是否继续查找：4.继续查找  5.修改名片  6.删除名片  0.返回上级菜单")
                    choice1=input("请再次选择功能：")
                    if choice1=="4":
                        chaZhao()
                        return          #退出迭代调用
                    elif choice1=="5":
                        i["name"]=xiugai(i,"name")
                        i["age"]=xiugai(i,"age")
                        i["phone_number"]=xiugai(i,"phone_number")
                        print("修改成功！修改后的名片如下：")
                        print("-" * 60)
                        print("姓名\t\t年龄\t\t电话号码")
                        print("%s\t\t%s\t\t%s" % (i["name"], i["age"], i["phone_number"]))
                        print("-" * 60)
                    elif choice1=="6":
                        message_list.remove(i)
                        print(" 删除成功！")
                        return
                    elif choice1=="0":
                        return          #直接退出函数返回上级菜单
                    else:
                        print("输入错误，请重新输入!")
        else:
            print("没有此名片信息！")
            while True:
                print("是否继续查找：4.继续查找  0.返回上级菜单")
                choice1 = input("请再次选择功能：")
                if choice1 == "4":
                    chaZhao()
                    return
                elif choice1 == "0":
                    return
                else:
                    print("输入错误，请重新输入!")
    #message_list=[{"name":"q","age":"w","phone_number":"e"}] 全局变量在函数中若干问题

def xinJian():
    name=input("请输入添加的姓名：")
    age=input("请输入添加的年龄：")
    phone_number=input("请输入添加的手机号：")
    xinjian_dict={"name":name,"age":age,"phone_number":phone_number}
    message_list.append(xinjian_dict)   #使用方法来修改全局变量的值在函数中，不是赋值
    print("已添加如下名片信息：")
    print("-" * 60)
    print("姓名\t\t年龄\t\t电话号码")
    print("%s\t\t%s\t\t%s" % (xinjian_dict["name"], xinjian_dict["age"], xinjian_dict["phone_number"]))
    print("-" * 60)
    while True:
        print("是否继续添加：7.继续添加  0.返回上级菜单")
        choice2=input("请再次选择功能：")
        if  choice2=="7":
            xinJian()
            return
        elif choice2=="0":
            return
        else:
            print("输入错误！请重新输入：")

def xiugai(message_xiugai,string):
    if string=="name":
        xiugai_value=input("修改后的姓名为（回车不修改哦）：")
        if len(xiugai_value)>0:
            return xiugai_value
        else:
            return message_xiugai["name"]
    if string=="age":
        xiugai_value=input("修改后的年龄为（回车不修改哦）：")
        if len(xiugai_value)>0:
            return xiugai_value
        else:
            return message_xiugai["age"]
    if string=="phone_number":
        xiugai_value=input("修改后的手机号为（回车不修改哦）：")
        if len(xiugai_value)>0:
            return xiugai_value
        else:
            return message_xiugai["phone_number"]

def xianShi():
    if len(message_list)==0:
        print("没有任何名片信息！请先填加!")
        return
    print("所有名片信息如下：")
    print("-" * 60)
    #for biaotou in ["姓名","年龄","电话号码"]:
     #   print( biaotou,end='\t\t')
    #print("")
    print("姓名\t\t年龄\t\t电话号码")
    for j in message_list:
        print("%s\t\t%s\t\t%s" % (j["name"], j["age"], j["phone_number"]))
    else:
        print("-" * 60)
        print("显示完毕！")
    while True:
        print("是否返回：0.返回上级菜单")
        choice3=input("请再次选择功能：")
        if choice3=="0":
            return
        else:
            print("输入错误！请重新输入：")



