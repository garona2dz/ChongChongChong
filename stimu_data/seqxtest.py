import readtxt

list1 = readtxt.pos_x
list2 = readtxt.pos_y
data_list_y = []
data_list_x = []
m = 0

while m < len(readtxt.pos_y):
    n = 0
    while n < len(readtxt.pos_x):
        data_list_x.append(list1[n])
        n += 1
    m +=1

print(data_list_x)
print(len(data_list_x))

file_x =open("/Users/garona/Desktop/seq_x.txt",'w')
file_x.write(str(data_list_x))