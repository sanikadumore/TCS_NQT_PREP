#refer to the same object
a=[1,2,3]
b=a
c=[1,2,3]
print(a is b)#true
print(a is c)#false
print(a==c)#true
# is op checks the object identity
# == checks value equality