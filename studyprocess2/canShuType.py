tu=(3,3,4,5)
lis=[4,5,6,7]
print(tu)
print(lis)
li=[0,1,2,3]
lii=(0,1,2,3)

def fun(a,*b,**c):
    print(a)
    print(type(b))
    print(b)
    print(type(c))
    print(c)

fun(100,333,li,lii,b=2,c=3)