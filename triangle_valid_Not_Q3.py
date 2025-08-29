3. ###Write a program to input angles of a triangle and check whether triangle is valid or not.
triangle1 = int(input("Enter angle of triangle1:"))
triangle2 = int(input("Enter angle of triangle2:"))
triangle3 = int(input("Enter angle of triangle3:"))
if(triangle1 > 0 and triangle2 > 0 and triangle3 > 0):
    if(triangle1 + triangle2 + triangle3 == 180):
        print(f'The triangle is valid.')
    else:
        print(f'The triangle is not valid.')
else:
    print(f'Invalid triangle.')