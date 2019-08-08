import readtxt

list1 = readtxt.pos_x
list2 = readtxt.pos_y
data_list_y = []
data_list_x = []
i = 0

while i < len(readtxt.pos_y):
    j = 0
    while j < len(readtxt.pos_x):
        data_list_y.append(list2[i])
        j += 1
    i += 1
pass

print(data_list_y)
print(len(data_list_y))


file_y =open("/Users/garona/Desktop/seq_y.txt",'w')
file_y.write(str(data_list_y))