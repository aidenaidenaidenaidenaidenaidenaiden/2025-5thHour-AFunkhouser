#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: HW_R7


#1. Create a class containing a def function that inits self and the three attributes: name, grade, color.
class coolbeans:
    def __init__(self,name,grade,color):
        self.name = name
        self.grade = grade
        self.color = color
#2. Make a def function within the class that adds 1 to the grade attribute to any object called to it.
#If they are 12th grade, have the code change their grade to "graduated" instead.
    def grader(self):
        if self.grade == 12:
            self.grade = "Graduated"
        else:
            self.grade += 1
#3. Make a def function within the class that offers the user to input/change their favorite color.
    def colorer(self):
        ans = input("Would you like to change your favorite color? (Y/N) ")
        if ans == "Y":
            self.color = input("What's your favorite color?  ")