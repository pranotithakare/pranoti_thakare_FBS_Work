###7. Given two sets of numbers, write a Python program to find the missing numbers in the second 
# set as compared to the first and vice versa. Use the Python set.
# Define the two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1

print("Numbers in Set1 but missing in Set2:", missing_in_set2)
print("Numbers in Set2 but missing in Set1:", missing_in_set1)
