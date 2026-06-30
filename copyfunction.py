#list function=copy()
#creates a copy of the list
list=[1,2,3,4,5]
list2=list.copy()
print(list2)

list3=[]
for i in list:
    list3+=[i]
print(list3)

list4=[]
i=0
while i<len(list):
    list4+=[list[i]]
    i+=2
print(list4)
