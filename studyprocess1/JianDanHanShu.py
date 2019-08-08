def print_lines(char,times,rows):
    """打印多行字符"""
    row=1
    while(row<=rows):
        print(char*times)
        row+=1

print_lines("@",9,3)



