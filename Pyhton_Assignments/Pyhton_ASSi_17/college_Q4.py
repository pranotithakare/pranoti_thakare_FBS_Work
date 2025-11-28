###4. Create a class College which has collection of students. 
# Add the following methods :

#a. Parameteried constructor for number of students.
#b. AddStudent
#c. GetStudent
#d. RemoveStudent
#e. Override __str__ Method


class College():
    def __init__(self,number_of_students):
        self.students = []
        self.num_of_stud = number_of_students
    def addStudent(self,student_name):
        if(len(self.students) < self.num_of_stud):
            self.students.append(student_name)
            print(f'students {student_name} added.')
        else:
            print(f'cannont add more students .')

    def getStudent(self,index):
        if 0 <= index < len(self.students):
            return self.students[index]
        else:
            return "Invalid index"
    
    def removeStudent(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"Student '{student_name}' removed.")
        else:
            print(f"Student '{student_name}' not found.")
    
    def __str__(self):
        return f"College with {len(self.students)} student(s): {', '.join(self.students)}"
    
college = College(3)  # College can have 3 students

college.addStudent("pranu")
college.addStudent("mau")
college.addStudent("anmol")
college.addStudent("nehu")  # Should not be added (exceeds capacity)

print(college.getStudent(1))  # Output:pranu
print(college.getStudent(5))  # Invalid index

college.removeStudent("pranu")
college.removeStudent("abc")  # Not in list

print(college)  # Uses __str__ met


        


