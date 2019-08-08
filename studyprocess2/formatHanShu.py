age=20
name='Swaroop'
print('{} was {} years old when he wrote this book.'.format(name,age))
print('Why is {} playing with that python?'.format(name))
print('{0} was {1} years old when he wrote this book.'.format(name,age))
print('Why is {0} playing with that python?'.format(name))

print('{0:.3f}'.format(1.0/3))
print('{0:*^11}'.format('hello'))
print('{name} wrote {book}'.format(name='Swaroop',book='A byte of Python'))

print('a',end=' ')
print('b',end='')
print('c',end='&')
print('\n')
print("代码换\
hhhhh行")

s='''this is a multi-line string.
h
this is the second line.'''
print(s)