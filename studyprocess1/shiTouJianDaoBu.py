import random
print ("石头：1;剪刀：2;布：3")
player=int (input("请输入要出的拳头👊:"))
computer=random.randint (1,3)
print("玩家出的是:%d ，电脑出的是:%d" %(player,computer))
if ((player==1 and computer==2)
        or(player==2 and computer==3)
        or(player==3 and computer==1)):
    print ("你赢了！")
elif (player==computer):
    print("彼此彼此！")
else:
    print("你输了！")


