###9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)
m1 = int(input("Enter marks of subject 1:"))
m2 = int(input("Enter marks of subject 2:"))
m3 = int(input("Enter marks of subject 3:"))
m4 = int(input("Enter Marks of subject 4:"))
m5 = int(input("Enter marks of suject 5:"))
total_marks = m1 + m2 + m3 + m4 + m5
percentage = (total_marks / 500) * 100

print(f"\nTotal Marks: {total_marks}/500")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 75:
    print("Grade: Distinction")
elif percentage >= 60:
    print("Grade: First Class")
elif percentage >= 50:
    print("Grade: Second Class")
elif percentage >= 35:
    print("Grade: Pass")
else:
    print("Grade: Fail")