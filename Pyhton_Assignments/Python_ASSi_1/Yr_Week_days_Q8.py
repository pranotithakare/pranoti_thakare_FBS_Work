###8. Write a program to convert days into years, weeks and Input total number of days

total_days = int(input("Enter total number of days:"))

year =  total_days // 365
total_days = total_days % 365

weeks = total_days // 7
total_days = total_days % 7
print(f'Total number of days is {total_days}')