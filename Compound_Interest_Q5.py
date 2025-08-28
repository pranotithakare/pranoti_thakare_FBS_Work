###Write a program to enter P, T, R and calculate Compound Interest.
P = int(input("Enter principal amount:"))
R = int(input("Enter rate of interest:"))
T = int(input("Enter time of year:"))
CI = P * ((1 + R / 100) ** T) - P
print(f'Compound Interest is {CI}')