#index function
#index() returns the index positon of the 1st occurance
#of the specified value
tuple=(1,2,3,1,1,2,2,3,4)
print(tuple.count(3))
print(tuple.count(4))

search=20
for i in range (len(tuple)):
    if tuple[i]==search:
        print("index=",i)
        break

tuple=(1,2,3,1,1,2,2,3,4,"siya","siya")
print(tuple.count("siya"))
print(tuple.count(3))
search=2
count1=1
for i in tuple:
    if i==search:
        count1+=1
        
        print("count of 2=",count1)