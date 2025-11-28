##2. Python Program to Remove the nth Index Character from a Non-Empty String

def remove_nth_char(text, n):
    
    return text[:n] + text[n+1:]

str1 = "Firstbit"
n = 4 
res = remove_nth_char(str1, n)
print("Original String:", str1)
print("Modified String:", res)
