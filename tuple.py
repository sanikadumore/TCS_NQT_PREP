#what is tuple?
#what is tu#it is a collection data type
#it is collection data structure list tuple set dictionary
#tuple is a built in python data type
#used to stored the multiple value in a single variable
#it is ordered and mutable collection
#which means once a tuple is created its elements its elements cannot be removed or added
#syntax of tuple
#tuple_name=(val1 val2)

student=("riya",24,"python")
print(student)

student=("riya",24,"python")
print(type(student))
print(student)

#characteristics of tuple
#ordered
tuple=(1,2,3,4,5)#(0,1,2,3,4)
print(tuple[4])

#index wise data insert
#immutable you cannot modify elements after creation
tuple1=(10,20,30,40,50)
tuple1[2]=50
print(tuple1)

#allows duplicate values
#can store different data types
tuple2=(1,2,3,1,1,2,2,3,3,"A","siya",34.55)
print(tuple2)
#support negative indexing
#0 start last size size-1=-1,-2.-3
tuple3=(10,20,30,40,50,60)
#+ve indexing=(0,1,2,3,4,5)   -ve indexng=(-1,-2,-3,-4)
print(tuple3[-1])



