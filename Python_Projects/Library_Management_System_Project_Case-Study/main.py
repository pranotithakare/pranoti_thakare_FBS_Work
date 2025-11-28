from admin import Admin
from getpass import getpass
import csv
import os

ADMIN_FILE = 'Core_Python/Demos/Basics/LMS_Project_CaseStudy/data/password.csv'

#Create admin.csv if not exists
if not os.path.exists(ADMIN_FILE):
    with open(ADMIN_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["username", "password"])
        writer.writerow(["admin", "pranu@123"])  # default login

max_attempts = 3
attempts = 0

while True:
    print('''\nPlease select choice:
    1. Login
    2. Exit''')

    ch = input("Enter choice: ")

    if ch == '1':
        while attempts < max_attempts:
            uname = input('Enter name: ')
            passw = getpass('Enter password: ')

            # Step 2: Check credentials from CSV file
            with open(ADMIN_FILE, "r") as f:
                reader = csv.DictReader(f)
                users = list(reader)

            #valid = any(u["username"] == uname and u["password"] == passw for u in users)
            valid = False
            for u in users:
                if u["username"] == uname and u["password"] == passw:
                  valid = True
                  break

            if valid:
                print('\n\U00002705 Logged in successfully...')
                a = Admin(ADMIN_FILE )  # open admin menuadmin
                
                break
            else:
                attempts += 1
                print(f'Invalid credentials... Attempts left: {max_attempts - attempts}')

        if attempts == max_attempts:
            print('\n\U000026A0 All login attempts exhausted. Please try again later.')
            break

    elif ch == '2':
        print('\n\U0001F44B Thanks for choosing us!')
        break

    else:
        print('\nInvalid choice...')
