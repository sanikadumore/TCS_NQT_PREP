#append() #insert()

#append function in list
#used=add one element at the end of elements
list=[1,2,3,4,5]
list.append(89)
list.append(76)
#insert function=inserta an elements at a specific index
# syntax=list.insert(indexnumber,value)
list.insert(1,34)
print(list)
list.insert(9,34)
print(list)
list.insert(-1,34)
print(list)
#extend()=adds all elementsof another list to the current list
list1=[1.2,3]
list2=[4,5,6]
list1.extend(list2)
#list2 value are shifted to list1 4 5 6 are shifted to 1 2 3
print(list1)#[1 2 3 4 5 6]
list1=[1.2,3]
list2=[4,5,6]
list2.extend(list1)#123456 are shifte to 456
print(list2)#[4 5 6] [1 2 3 4 5 6]

#remove()=removes the first occurence of the specified value
num=[10,20,30,40,20,20]
num.pop(5)
num.remove(30)
print(num)
#del num[:-1]
print(num)