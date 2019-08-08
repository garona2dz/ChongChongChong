# string[begin index:end index:step]

string="0123456789"
string1=string[:] #全取
print(string1)
string2=string[-1::-1] #逆序
print(string2)
string3=string[::2] #取偶数项
print(string3)
string4=string[1::2] #取奇数项
print(string4)
string5=string[-3:] #取末尾
print(string5)
string6=string[-3:-1] #取末尾不带最后项
print(string6)
