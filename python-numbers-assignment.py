P=3.14
x=75
print(P,type(P),sep=',')
print(x,type(x),sep=',')

x=1+2j
y=1+2J
print(x,type(x),sep=',')
print(y,type(y),sep=',')


import sys
x=123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
print("value is :",x)
print("size is :",sys.getsizeof(x))
print("type is :",type(x))
