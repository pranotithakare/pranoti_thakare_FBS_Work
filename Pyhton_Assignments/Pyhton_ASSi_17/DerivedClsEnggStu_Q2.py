###2. Create a derived class from Student as EnggStudent with :
###a. Data members as :
#i. Branch
#ii. InternalMarks

####b. Add the following methods :
#i. Parameterized constructor
#ii. Display
#iii. Accept
#iv. override Method CalculateRank
#v. Override __str__ Method

from student_Q1 import Student

class EnggStudent(Student):
    def __init__(self,student_id,name,age,percentage,branch,internal_marks):
        super().__init__(student_id,name,age,percentage)
        self.Branch = branch
        self.InternalMarks = internal_marks

    def Display(self):
        super().Display()
        #f'BRANCH:{self.Branch}\nINTERNALMARKS:{self.InternalMarks}'
        print(f'BRANCH: {self.Branch}')
        print(f'INTERNALMARKS: {self.InternalMarks}')

    
    def Accept(self):
        super().Accept()
        self.branch = input("Enter a branch name :")
        self.internal_marks = float(input("enter internal marks :"))
    
    def CalculateRank(self):
        total_perc = self.Percentage * 0.7 + self.InternalMarks * 0.3
        if(total_perc >= 90):
          self.Rank = 1
        elif(total_perc >= 80):
            self.Rank = 2
        elif(total_perc >= 70):
            self.Rank = 3
        else:
            self.Rank = 4
    def __str__(self):
        return f'STUDENT_ID:{self.StudentId}\nNAME:{self.Name}\nAGE:{self.Age}\nPERCENTAGE:{self.Percentage}\nRANK:{self.Rank}\nBRANCH:{self.Branch}\nINTERNALMARKS:{self.InternalMarks}'

# e1 = EnggStudent(1,'mau',22,90,'CS',90)
# e1.Display()
# e1.Accept()
# e1.CalculateRank()
# print("After Calculating rank")
# print(e1)
        






