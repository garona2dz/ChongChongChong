list1 = [9, 3, 7, 6, 5, 4]
list2 = [1, 2, 3, 4, 5, 6]
list3 = [5, 4, 3, 2, 1]

def insert_sort1(deal_list):
    i=1
    while i < len(deal_list):
        item = deal_list[i]
        j = i - 1
        while j >= 0:
            if item <= deal_list[j]:
                temp = deal_list[j]
                deal_list[j] = item
                deal_list[j + 1] = temp
            j -= 1
        i += 1
    print(deal_list)


def insert_sort2(deal_list):
    i = 1
    while i < len(deal_list):
        item = deal_list[i]
        j = i - 1
        while j >= 0:
            if item < deal_list[j]:
                deal_list[j + 1] = deal_list[j]
                j -= 1
            else:
                break  # 如果要插入的项大于前一项则就不用再比较之前的项了
        deal_list[j + 1] = item
        i += 1
    print(deal_list)



insert_sort1(list1)
insert_sort1(list2)
insert_sort1(list3)

insert_sort2(list1)
insert_sort2(list2)
insert_sort2(list3)