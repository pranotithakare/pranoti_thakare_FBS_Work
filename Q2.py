###Q2.Write a program to calculate simple interest based on Principal, Rate and Time (SI = P*R*T/100)

P = int(input("Enter the principal amount: "))
R = int(input("Enter of interest: "))
T = int(input("Enter the time of yr: "))
 
SI = (P * R * T) / 100
print(f'Simple Interest = ', SI)
