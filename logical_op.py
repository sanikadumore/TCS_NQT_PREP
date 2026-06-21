#used to combined operation 
#and used if both conditions are true
# or true if at least one condition is true
#not reverses the value or result

age=21
print("AND op",age>18 and age<25)#true
print("OR op",age>18 or age<20)#true
print("NOT op",not(age>30))#true
print(age>30)#false


#truth table for AND operator
#A  B   A and B  A or B  A xor^ B
#0  0      0       0       0
#1  0      0       1       1
#0  1      0       1       1 
#1  1      1       1       0