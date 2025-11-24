###1. Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.

# userid = input("Enter User ID: ")
# password = input("Enter Password: ")


correct_userid = "admin"
correct_password = "1234"

for attempt in range(1, 4):
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == "admin" and password == "1234":
        print("Login successful!")
        break
    else:
        print(f"Invalid credentials. Attempt {attempt} of 3.\n")
else:
    print("Too many failed attempts. Access denied.")
