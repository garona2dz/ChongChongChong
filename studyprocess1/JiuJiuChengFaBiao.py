i=1
result=0
while i<=9:
    j = 1
    while j<=i:
        result=i*j
        print("%d*%d=%d" %(j,i,result),end="\t")
        j+=1
    i+=1
    print("")