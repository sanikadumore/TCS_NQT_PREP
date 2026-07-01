#nested tuple means tuple  inside tuple
data=( 
    ("siya",66),
    ("riya",65),
    ("priya",44)
)
print(data)
for name,marks in data:
    print(name,"=",marks)