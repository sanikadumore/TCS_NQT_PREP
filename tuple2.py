#unpack the data
#print tne fist value in tuple without indexing or loop
student=("siya",24,"python")
print(student)
name,age,course=student
print(name)

student=("siya",24,"python")
print(student)
print(student[0])
for i in student:
    if i=="siya":
        print(i)
        break
name,age,course=student
print(name)