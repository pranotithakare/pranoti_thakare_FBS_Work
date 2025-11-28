###1. Create a class Student with following
###a. data members :
#i. StudentId
#ii. Name
#iii. Age
#iv. Percentage

###b. Add the following methods :
#i. Parameterized constructor
#ii. Display
#iii. Accept
#iv. Method CalculateRank
#v. Override __str__ Method

class Student:
    def __init__(self,student_id,name,age,percentage):
        self.StudentId = student_id
        self.Name = name
        self.Age = age
        self.Percentage = percentage
        self.Rank = 0


    def Display(self):
        f'STUDENT_ID:{self.StudentId}\nNAME:{self.Name}\nAGE:{self.Age}\nPERCENTAGE:{self.Percentage}'
        # if self.Rank is not 0:
        #     print(f"Rank : {self.Rank}")

    def Accept(self):
        self.StudentId = input("Enter a id:")
        self.Name = input("Enter a name: ")
        self.Age = int(input("Enter a age: "))
        self.Percentage = float(input("Enter a percentage: "))

    def CalculateRank(self):
        if(self.Percentage >= 90):
            self.Rank = 1
        elif(self.Percentage >= 80):
            self.Rank = 2
        elif(self.Percentage >= 70):
            self.Rank = 3
        else:
            self.Rank = 4
        
    def __str__(self):
        return f'STUDENT_ID:{self.StudentId}\nNAME:{self.Name}\nAGE:{self.Age}\nPERCENTAGE:{self.Percentage}\nRANK:{self.Rank}'
    
# s1 = Student(101,"mau",22,85.7)
# s1.Display()
# s1.Accept()
# s1.CalculateRank()
# print("\nAfter calculating rank:")
# print(s1)

        