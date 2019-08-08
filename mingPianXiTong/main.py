#! /usr/local/bin/python3
import tool

while True:
    print("*"*36)
    print("欢迎使用系统：")
    print("1.查找名片")
    print("2.新建名片")
    print("3.显示全部")
    print("0.退出系统")
    print("*"*36)
    choice=input("请选择功能：")
    if choice in ["0","1","2","3"]:
        if choice=="0":
            tool.tuiChu()
            break
        elif choice=="1":
            tool.chaZhao()
        elif choice=="2":
            tool.xinJian()
        elif choice=="3":
            tool.xianShi()
    else:
        print("输入错误，请重新输入!")

