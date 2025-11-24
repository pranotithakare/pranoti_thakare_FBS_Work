###8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
beg = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(beg, end + 1):
    if(num % 7 == 0 and num % 5 == 0):
        print(num)
