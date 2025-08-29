###7. Write a program to check if user has entered correct userid and password.
u_id = input("Enter User id:")
password = input("Enter password:")
if(u_id == 'pranu27'):
    if(password == 'pranu@123'):
        print(f'Log in successful.')
    else:
        print(f'Incorrect password.')
else:
    print(f'Incorrect user id.')


