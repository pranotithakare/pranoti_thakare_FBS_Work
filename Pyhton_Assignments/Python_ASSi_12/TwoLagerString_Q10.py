###10.Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions.
def get_length(s):
    count = 0
    for char in s:
        count += 1
    return count

def display_larger_string(str1, str2):
    len1 = get_length(str1)
    len2 = get_length(str2)

    if len1 > len2:
        return str1
    elif len2 > len1:
        return str2
    else:
        return "Both strings are equal in length"

s1 = "Python"
s2 = "JavaScript"

res = display_larger_string(s1, s2)
print("Larger String:", res)
