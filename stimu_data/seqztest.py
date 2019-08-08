file3 = "/Users/garona/Desktop/z.txt"
pos_z =[]
with open(file3, 'r') as file3_to_read:
    while True:
        lines = file3_to_read.readline()
        if not lines:
            break
        for l in lines.split():
            pos_z.append(float(l))
file3_to_read.close()
print(pos_z)
print(len(pos_z))

file_z =open("/Users/garona/Desktop/seq_z.txt",'w')
file_z.write(str(pos_z))