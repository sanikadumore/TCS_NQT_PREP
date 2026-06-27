#function with arguments +with return
def addition(a,b,c):
    return a+b+c
a,b,c=map(int,input("enter 3 values").split())
print("addition=",addition(a,b,c))

def additionn(a,b,c):
    c=a+b+c
    return a+b+c
    return c