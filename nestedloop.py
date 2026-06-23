#nested loop =a loop inside another loop
#for:
#   for(:)

for i in range (3):
    for j in range(2):
        print(i,j)
#0 0
#0 1
#1 0
#1 1
#2 0
#2 1

for i in range (3):
    print("value of i=",i)
    for j in range(2):
        print("value of i=",i,"value of j=",j)

#value of i= 0
#value of i= 0 value of j= 0
#value of i= 0 value of j= 1
#value of i= 1
#value of i= 1 value of j= 0
#value of i= 1 value of j= 1
#value of i= 2
#value of i= 2 value of j= 0
#value of i= 2 value of j= 1
for i in range (3):
    print("value of i=",i)
    print("\n")#\n use for new line
    for j in range(2):
        print("value of i=",i,"\t""value of j=",j)

