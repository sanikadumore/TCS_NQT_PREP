tuple=(1,2,3,4,5,6,756,34,78,45,66)
print("max=",max(tuple))

#hard code logic for max function in the tuple
maxvalue=tuple[1]
for i in tuple:
    if i>maxvalue:#1>2 2>2 3>2 4>3 5>4
        maxvalue=i#3 4 5       756
print("max value using for loop=",maxvalue)

