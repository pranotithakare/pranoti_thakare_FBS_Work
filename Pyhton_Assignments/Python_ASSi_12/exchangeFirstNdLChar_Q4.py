###4. Python Program to Form a New String where the First Character and the Last Character 
# have been Exchanged


def exchangeFNdLChar(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + s[1:-1] + s[0]


str1 = "python"
new_str = exchangeFNdLChar(str1)
print("Original String:", str1)
print("New String:", new_str)
