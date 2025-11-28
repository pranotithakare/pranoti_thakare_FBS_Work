###3. Create a class MedicalStudent inherited from Student with following
###Data members :

#i.Specialization
#ii. MarksOfInternship

####b. Add the following methods :
#i. Parameterized constructor
#ii. Display
#iii. Accept
#iv. override Method CalculateRank
#v. Override __str__ Method


from student_Q1 import Student
class MedicalStudent(Student):
    def __init__(self,student_id,name,age,percentage,specialization,marksofinternship):
        super().__init__(student_id,name,age,percentage)
        self.Specialization = specialization
        self.MarksOfInternship = marksofinternship

    def Display(self):
        super().Display()
        #f'BRANCH:{self.Branch}\nINTERNALMARKS:{self.InternalMarks}'
        print(f'SPECIALIZATION: {self.Specialization}')
        print(f'MARKSOFINTERNSHIP: {self.MarksOfInternship}')

    
    def Accept(self):
        super().Accept()
        self.specialization = input("enter a Specialization  :")
        self.marksofinternship = float(input("enter marks of internship marks :"))
    
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

e1 = MedicalStudent(1,'mau',22,90,'Gynacologist',87)
e1.Display()
e1.Accept()
e1.CalculateRank()
print("After Calculating rank")
print(e1)
        






