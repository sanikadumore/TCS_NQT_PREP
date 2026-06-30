#list function=index()
#returns the index of the 1st occurence if the the given value
data=["riya","siya1","jiya","priya","siya","siya"]
print(data.index("siya"))
#for i in data:
#   if (i=="ram"):
#      print(i)
#      print(number)
#     number+=1
for i in range (len(data)):
     if data[i] =="siya":
        print("index=",i,"value=",data[i])
