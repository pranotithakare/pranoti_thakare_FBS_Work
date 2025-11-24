###2. Enter number of students from user. For those many students accept marks of 5  
#subject marks from user and calculate percentage. Display all percentage and  
#average percentage of students.
num_students = int(input("Enter number of students: "))
total_percentage = 0

for i in range(1, num_students + 1):
    print(f"\nEnter marks for Student {i}:")
    total = 0
    for j in range(1, 6):
        marks = float(input(f" Marks of Subject {j}: "))
        total += marks

    percentage = (total / 500) * 100
    print(f"  → Percentage = {percentage}%")

    total_percentage += percentage

average = total_percentage / num_students
print(f"\nAverage Percentage of all students: {average}%")
