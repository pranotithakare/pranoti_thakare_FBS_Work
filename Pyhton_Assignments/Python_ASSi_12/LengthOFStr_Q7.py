###7. Python Program to Calculate the Length of a String Without Using a Library Function
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

str1 = "Data Structure"
length = string_length(str1)
print("Original String:", str1)
print("Length of the string:", length)
