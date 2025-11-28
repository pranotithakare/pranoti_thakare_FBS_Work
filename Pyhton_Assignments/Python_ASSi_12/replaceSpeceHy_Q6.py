###6. Python Program to Take in a String and Replace Every Blank Space with Hyphen

def replace_space_with_hyphen(s):
    new_str = ""
    for char in s:
        if char == " ":
            new_str += "-"
        else:
            new_str += char
    return new_str
str1 = "Hello World Python"
new_str = replace_space_with_hyphen(str1)
print("Original String:", str1)
print("Modified String:", new_str)
