#Add, remove, view users
import csv
import os
import re

class Users:
    def __init__(self):
        # Define file path
        self.file_path = 'Core_Python/Demos/Basics/LMS_Project_CaseStudy/data/users.csv' 
        
        
        if not os.path.exists('Core_Python/Demos/Basics/LMS_Project_CaseStudy/data/users.csv'):
            with open('Core_Python/Demos/Basics/LMS_Project_CaseStudy/data/users.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["UserID", "UserName", "Email", "Contact"])

    
    def addUser(self):
        
        existing_ids = set()
        existing_names = set()
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as fp:
                reader = csv.reader(fp)
                next(reader, None)  
                for row in reader:
                    if len(row) >= 2:
                        existing_ids.add(row[0].strip())
                        existing_names.add(row[1].strip().lower())

        #Input details with uniqueness check using exception
        try:
            user_id = input('Enter User ID: ').strip()
            if user_id in existing_ids:
                raise ValueError('User ID already exists.')

            name = input('Enter User Name: ').strip()
            if name.lower() in existing_names:
                raise ValueError('User Name already exists.')
            #Email Validation
            email = input('Enter User Email: ').strip()
            email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        
            if not re.match(email_pattern, email):
                raise ValueError('Invalid email format. Please enter a valid email.')
            
            mob_no = input('Enter Contact Number: ').strip()

          
            with open(self.file_path, 'a', newline='') as fp:
                writer = csv.writer(fp)
                writer.writerow([user_id, name, email, mob_no])

            print('\U00002705 User added successfully!\n')

        except ValueError as ve:
            print(ve)
            print('Please try again.\n')
        except Exception as e:
            print('An unexpected error occurred:', e)

    def removeUser(self):
        user_id = input('Enter User ID to remove: ').strip()
        users = []
        removed = False

        with open(self.file_path, 'r', newline='') as fp:
            reader = csv.reader(fp)
            for row in reader:
                if not row:  # skip empty rows
                  continue
                if row[0] != user_id:#If we find a user whose ID matches the given ID, we delete that user.
                   users.append(row)
                else:
                   removed = True

        with open(self.file_path, 'w', newline='') as fp:#write new list back to the file.
            writer = csv.writer(fp)
            writer.writerows(users)

        if removed:
           print('\u274C User removed successfully!\n')
        else:
            print('\u274C User ID not found!\n')


    def viewUsers(self):
        print("\n All Registered Users:")
        with open('Core_Python/Demos/Basics/LMS_Project_CaseStudy/data/users.csv', 'r', newline='') as fp:
            reader = csv.reader(fp)
            for row in reader:
                print(row)
        print()

