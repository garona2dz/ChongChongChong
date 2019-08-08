list1 = [2, 4, 5, 3, 1]
list2 = [3, 2, 1, 5, 4]


def selection_sort1(deal_list):
    i = 0
    while i <= len(deal_list) - 2:
        j = i + 1
        while j <= len(deal_list) - 1:
            if deal_list[i] >= deal_list[j]:
                temp = deal_list[j]
                deal_list[j] = deal_list[i]
                deal_list[i] = temp    # 直接交换赋值，直到把最小值放在最小位置
            j += 1
        i += 1
        # print(list)
    return deal_list


def select_sort2(lyst):
    i=0
    while i < len(lyst) - 1:
        min_index = i
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[min_index]:
                min_index = j     # 没有直接交换赋值，先标记最小位置，然后再将
            j += 1                # 最小位置直接和指定位置交换赋值，减少了赋值次数
        if min_index != i:
            temp = lyst[min_index]
            lyst[min_index] = lyst[i]
            lyst[i] = temp
        i +=1
    return lyst


print(list1)
print("-" * 16)
print(selection_sort1(list1))
print("*" * 16)
print(list2)
print(select_sort2(list2))






