#online shopping cart product added
#laptop mobilr torch keyboard mouse



cart=input("enter any 5 products").split
for cart in range(6):
    print("added")
print(type(cart))#str

for i in cart:
    print(i,"added succesfully")

cart=[]
for i in range(6):
    products=input("enter your products:")
    cart.append(products)

for i in cart:
    print(i,"added")

list=[1,2,3,4]
list.append(23)
list.append("hello python")
print(list)

list=[1,2,3,4]
list.append(23)
list.insert(2,34)#add
list.append("hello python")
print(list)

cart=[]
userinput=int(input("how many products do you want to add?"))
for i in range(userinput):
    products=input("enter your products:")
    cart.append(products)
for i in cart:
    print(i,"added")

cart=[]
userinput=int(input("how many products do you want to add?"))
for i in range(userinput):
    products=input(f"enter your products{i+1}:")
    cart.append(products)
for i in cart:
    print(i,"added")









