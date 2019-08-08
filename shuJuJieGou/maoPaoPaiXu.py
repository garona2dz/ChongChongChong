list1 = [3, 2, 5, 1, 4]
list2 = [5, 4, 3, 2, 1]
list3 = [1, 2, 3, 4, 5]


def bubble_sort1(deal_list):
    i = len(deal_list) - 1
    while i > 0:
        swapped = False
        j = 0
        while j < i :
            if deal_list[j] >= deal_list[j+1]:
                temp = deal_list[j]
                deal_list[j] = deal_list[j+1]
                deal_list[j+1] = temp
                swapped = True
                print("1",end= "*")
            j += 1
        if not swapped:   # 添加一个标记，记录是否进行过交换，如果没有就说明已经排好序了
            print()
            return deal_list
        i -= 1
    print()
    return deal_list

print(list3)
print(bubble_sort1(list1))




