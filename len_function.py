#len()=length of tuple
tuple=91,2,3,4,5,6,7,8,9
print("length=",len(tuple))

#hard code for lrn function
count=0
for i in tuple:
    count=count+1
print("using for loop length=",count)

count1=0
i=0
try:
   while True:
       tuple[i]
       count1+=1
       i+=1
except IndexError:
    pass

while i<9:
    count1+=1
    i+=1
    print("using while loop",count1)

