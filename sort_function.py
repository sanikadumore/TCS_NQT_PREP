tuple1=(4,3,6,5,1,2,8,8,3,9)
print(sorted(tuple1 ))

#hard coded logic for sorted function in tuple
#bubble sort using for loop
#while loop
#tuple1=(4,3,6,5,1,2,8,8,3,9)
#    j  j+i

list1=list(tuple1)
for i in range(len(list1)):
    for j in range(len(list1)-i-1):
        if list1[j]>list1[j+i]:#4>3
            list1[j],list1[i+j]=list1[j+i],list1[j]
            #a       , b       =b          , a
print(list1)

