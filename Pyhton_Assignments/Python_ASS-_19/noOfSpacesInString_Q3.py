# 3. Count the number of spaces in a string (take input from user)
str1 = input("Enter a string: ")
space_count = len([char for char in str1 if char == ' '])
print("Number of spaces:", space_count)
