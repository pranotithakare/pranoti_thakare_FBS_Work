###12. Python Program to count number of lowercase characters in a string.
def count_lowercase(s):
    count = 0
    for char in s:
        if char >= 'a' and char <= 'z':  
            count += 1
    return count
str1 = "Good Morning"
lower_count = count_lowercase(str1)

print("Original String:", str1)
print("Number of lowercase characters:", lower_count)
