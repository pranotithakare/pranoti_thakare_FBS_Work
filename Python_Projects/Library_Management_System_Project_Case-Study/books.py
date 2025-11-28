import os
from prettytable import PrettyTable
from datetime import datetime

class Books:
    def __init__(self):
        # Define file paths
        self.data_dir = r"C:\Users\Admin\Desktop\FBS\Core_Python\Demos\Basics\LMS_Project_CaseStudy\data"
        os.makedirs(self.data_dir, exist_ok=True)

        self.BOOK_FILE = os.path.join(self.data_dir, "books.csv")
        self.LOG_FILE = os.path.join(self.data_dir, "logs.csv")

    def log_action(self, msg):
        with open(self.LOG_FILE, 'a') as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {msg}\n")

    #ADD BOOK 
    def addBook(self):
        b_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

    #Check if Book ID already exists
        try:
            with open(self.BOOK_FILE, 'r') as f:
              for line in f:
                data = line.strip().split(',')
                if len(data) > 0 and data[0] == b_id:
                    print('Book ID already exists! Please use a unique ID.')
                    return
        except FileNotFoundError:
            pass

    #If not duplicate, add the book
        with open(self.BOOK_FILE, 'a') as f:
            f.write(f'{b_id},{title},{author},Yes\n')

        print('\U00002705 Book added successfully.')
        self.log_action(f'Book added: {title}')


    #REMOVE BOOK
    def removeBook(self):
        b_id = input('Enter Book ID to remove: ')

        if not os.path.exists(self.BOOK_FILE):
            print('\u274C No book file found!')
            return

        lines = open(self.BOOK_FILE).readlines()
        removed = False
        with open(self.BOOK_FILE, 'w') as f:
            for line in lines:
                if not line.startswith(b_id + ','):
                    f.write(line)
                else:
                    removed = True

        if removed:
            print('\U00002705 Book removed successfully.')
            self.log_action(f"Book removed: {b_id}")
        else:
            print('\u274C Book ID not found.')

    #VIEW BOOKS 
    def viewBooks(self):
        table = PrettyTable(["Book ID", "Title", "Author", "Available"])
        if not os.path.exists(self.BOOK_FILE):
            print('\u274C No books found.')
            return
        with open(self.BOOK_FILE) as f:
            for line in f:
                b_id, title, author, avail = line.strip().split(",")
                table.add_row([b_id, title, author, avail])
        print(table)



        
        