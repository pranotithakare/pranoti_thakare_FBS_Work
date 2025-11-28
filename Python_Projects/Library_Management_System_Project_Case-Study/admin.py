from users import Users
from books import Books
from transactions import Transactions
import emoji
#import os
import csv 

class Admin:
    #def __init__(self):
   
    def __init__(self, admin_file):
        self.admin_file = admin_file

        #self.admin_file = 'Core_Python/Demos/Basics/LMS_Project_CaseStudy/data/password.csv'
        u1 = Users()
        b1 = Books()
        trans = Transactions()
        
        ch = 0
        while(ch != '11'):
            print('''------------------------ \U0001F4DA  Library Management System Menu  \U0001F4DA -----------------------

            1.Add Book
            2.Remove Book
            3.View Books
            4.Add User
            5.Remove User
            6.View Users
            7.Issue Book
            8.Return Book
            9.View Logs
            10.Changed Password
            11.Exit''')
            ch = input('Enter Choice:')
            if(ch == '1'):
               b1.addBook()
            elif(ch == '2'):
                b1.removeBook()
            elif(ch == '3'):
                b1.viewBooks()
            elif(ch == '4'):
                u1.addUser()
            elif(ch == '5'):
                u1.removeUser()
            elif(ch == '6'):
                u1.viewUsers()
            elif(ch == '7'):
                trans.issueBook()
            elif(ch == '8'):
                trans.returnBook()
            elif(ch == '9'):
                trans.viewLogs()
            elif(ch == '10'):
                self.changePassword()
            elif(ch == '11'):
                print('Exit From Library Managemnt System...')
            else:
                print('Invalid Choice...')



    def changePassword(self):
        print("\n---- Change Password ----")

        old_password = input("Enter old password: ")

        rows = []
        with open(self.admin_file, 'r', newline='') as f:
           reader = csv.DictReader(f)
           rows = list(reader)
           #print(rows)

           if len(rows) == 0:
                print("\u274C No admin found in file.")
                return

        current_password = rows[0]["password"] # in first admin row to stored the password.

    # Check old password
        if old_password == current_password:
            new_password = input("Enter new password: ")
            rows[0]["password"] = new_password  # update password in memory

        #Write updated password to file
            with open(self.admin_file, 'w', newline='') as f:
              writer = csv.DictWriter(f, fieldnames=["username", "password"])
              writer.writeheader()
              writer.writerows(rows)

            print(f"\U00002705 Password changed successfully to: {new_password}")
        else:
            print("\u274C Incorrect old password.")


# if(__name__ == '__main__'):
#     a = Admin()