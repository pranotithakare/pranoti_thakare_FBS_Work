###11. WAP to check if given number Strong Number.
num = input("Enter a number: ")
sum_of_factorials = 0

for digit in num:
    fact = 1
    for i in range(1, int(digit)+1):
        fact *= i
    sum_of_factorials += fact

if sum_of_factorials == int(num):
    print(f"{num} is a Strong Number.")
else:
    print(f"{num} is NOT a Strong Number.")
