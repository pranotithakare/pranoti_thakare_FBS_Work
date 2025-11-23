###1.Write a p;rogram to calculate percentage of student using 5  subject marks.
m1 = int(input("Enter student marks of subject 1:"))
m2 = int(input("Enter student marks of subject 2:"))
m3 = int(input("Enter student marks of subject 3:"))
m4 = int(input("Enterstudent  marks of subject 4:"))
m5 = int(input("Enter student marks of subject 5:"))
total_marks = m1 + m2 + m3 + m4 + m5
per = (total_marks / 500) * 100
print(f'Percentage is {per}%')