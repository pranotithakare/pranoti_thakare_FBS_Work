basic_sal = 20000
n = int(input(" Enter number of employee:"))
#basic_sal = 20000
for i in range(1,n+1):
    print(f'Employee {i}.')

    da = 0.10 * basic_sal
    ta = 0.12 * basic_sal
    hra = 0.15 * basic_sal

    total = basic_sal + da + ta + hra
    print(f'basic salary is {basic_sal}.')
    print(f'da is 10% {da}.')
    print(f'ta is 12 % {ta}.')
    print(f'hra is 15% {hra}.')
    print(f'Total salaray is {total}.')

