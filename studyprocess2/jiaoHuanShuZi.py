a=1
b=2
#可以使用其他变量
c=a
a=b
b=c
print(a,b)

#不使用其他变量
a=a+b
b=a-b
a=a-b
print(a,b)

#利用python元组
a,b=(b,a)
print(a,b)
a,b=b,a #括号可以省略
print(a,b)