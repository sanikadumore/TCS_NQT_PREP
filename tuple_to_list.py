#convert from tuple to list type conversion

tuple1=(1,2,3,4,5)
print(type(tuple1))
list1=list(tuple1)
list1.append(9)
tuple1=tuple(list1)
print(type(list1))
print(tuple1)

tup=(1,2,3,4,5)
list1=list(tup)
list1.append(40)
tup=tuple(list1)
print(tup)