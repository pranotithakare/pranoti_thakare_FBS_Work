###15. Python Program to find larger string without using built-in functions.
def get_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

def larger_string(str1, str2):
    len1 = get_length(str1)
    len2 = get_length(str2)

    if len1 > len2:
        return str1
    elif len2 > len1:
        return str2
    else:
        return "Both strings are equal in length"

s1 = "Python"
s2 = "Programming"

res = larger_string(s1, s2)

print("String 1:", s1)
print("String 2:", s2)
print("Larger String:", res)
