###6. WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

basic_salary = float(input("Enter basic salary: "))

da = 0.10 * basic_salary   # Dearness Allowance
ta = 0.12 * basic_salary   # Travel Allowance
hra = 0.15 * basic_salary  # House Rent Allowance

total_salary = basic_salary + da + ta + hra

print(f"DA (10%): {da:}")
print(f"TA (12%): {ta:}")
print(f"HRA (15%): {hra:}")
print(f"Total Salary: {total_salary:}")
