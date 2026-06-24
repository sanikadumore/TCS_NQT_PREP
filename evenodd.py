#print even odd number without if else condition
#print the even odd num using only for loop withoutany condition
for i in range(11):
    if(i%2==0):
        print(i,"even number")
    else:
        print(i,"odd number")

for i in range(2,21,2):
    print(i,end=" ")#2 4 6 8 10 12 14 16 18 20

print("odd number")
for i in range(1,21,2):
    print(i,end=" ")#1 3 5 7 9 11 13 15 17 19 

#sum of 1st 10 natural numbers using only for loop
#1 2 3 4 5 6 7 8 9 10
addition=0
for i in range (1,11):
    addition=addition+i
print("addition=",addition)#addition=55

addition=0;
for i in range (1,11):
    #addition=addition+i
    addition+=i
    print(i,end=" ")
print("addition=",addition)#addition=55