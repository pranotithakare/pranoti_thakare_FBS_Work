###8. Python Program to Remove the Characters of Odd Index Values in a string.
def removeOddIndChar(s):
    new_str = ""
    for i in range(len(s)):
        if i % 2 == 0:    
            new_str += s[i]
    return new_str
str1 = "Object Oriented Programming"
res =removeOddIndChar(str1)
print("Original String:", str1)
print("Modified String:", res)
