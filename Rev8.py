#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: HW_R8


#1. Import all of HW_R7 into this assignment using the from/import function.
from Rev7 import *
#2. Create an object of three students in the classroom. Ask for their name, grade, and favorite color as need be.
S1 = coolbeans("Sam",10,"Pretty Pink")
S2 = coolbeans("Ivan",12,"Purple")
S3 = coolbeans("Dylan",12,"Red")
#3. Print the name of the first student.
print(S1.name)
#4. Use the def function from HW_R7 to bump the grade level of the second student up by 1. Print the new grade.
S2.grader()
print(S2.grade)
#5. Use the def function from HW_R7 to ask the third student to change their favorite color to something else.
#Print the new color.
S3.colorer()
print(S3.color)