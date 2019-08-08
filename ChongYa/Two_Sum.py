def twosum(list_in, target):

    pos1 = 0  # 第一个数的索引
    pos2 = 0  # 第二个数的索引
    start = 0  # 代表每次查询的位置与初始的偏离

    while True:
        num1 = list_in[start - start]  # 每次从新的列表的第一个位置查找
        num2 = target - num1
        del list_in[list_in.index(num1)]  # 每次将查找的元素删除，避免重复
        if num2 in list_in:
            pos1 = start
            pos2 = list_in.index(num2) + start + 1
            break
        start += 1  # 每次查找由于删除了元素，所以要还原新列表的索引
        if len(list_in) == 1:
            break
    return [pos1, pos2]