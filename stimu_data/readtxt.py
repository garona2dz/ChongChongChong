file1 = "/Users/garona/Desktop/x.txt"
pos_x =[]
with open(file1,'r') as file1_to_read:
    while True:
        lines = file1_to_read.readline()
        if not lines:
            break
        for l in lines.split():
            pos_x.append(float(l))
file1_to_read.close()

file2 = "/Users/garona/Desktop/y.txt"
pos_y =[]
with open(file2,'r') as file2_to_read:
    while True:
        lines = file2_to_read.readline()
        if not lines:
            break
        for k in lines.split():
            pos_y.append(float(k))
file2_to_read.close()

print(pos_x)
print(pos_y)
