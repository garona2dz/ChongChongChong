def two_sum(list_in, target):  # 比leetcode上的twosum题要求要高，输出所有可能的索引
    list_out = []
    pos1 = []
    pos2 = []
    start = 0
    list_mid = list_in.copy()  # copy是浅复制，但由于没有子对象，所以相当于深复制
    while True:
        num1 = list_mid[start]
        num2 = target - num1
        del list_mid[list_mid.index(num1)]
        if num2 in list_mid:
            pos1.append(list_in.index(num1))
            list_in[list_in.index(num1)] = 'dz'
            pos2.append(list_in.index(num2))
            list_in[list_in.index(num2)] = 'dz'
            del list_mid[list_mid.index(num2)]
        if len(list_mid) == 0:
            break

    for i in range(0, len(pos1)):
        list_out.append([pos1[i], pos2[i]])

    for some in list_out:
        print(some)
        # return some # 如何返回多个结果


list1 = [0, 3, 6, 9]
two_sum(list1, 9)