try:
    num = int(input("请输入整数："))
    result = 8/num
    print(result)
except ValueError:
    print("请输入正确的整数格式！")
#except ZeroDivisionError:
#    print("分母不能为0")
except Exception as result:
    print("未知错误！%s" % result)  # 捕获未知错误

