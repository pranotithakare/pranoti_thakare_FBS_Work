import os
from datetime import datetime
from prettytable import PrettyTable

class Transactions:
    FINE = 50

    def __init__(self):
        self.BASE_PATH = os.path.join(os.path.dirname('Core_Python/Demos/Basics/LMS_Project_CaseStudy/transactions.py'), "data")
        self.BOOK_FILE = os.path.join(self.BASE_PATH, "books.csv")
        self.USER_FILE = os.path.join(self.BASE_PATH, "users.csv")
        self.ISSUED_FILE = os.path.join(self.BASE_PATH, "issued_books.csv")
        self.LOG_FILE = os.path.join(self.BASE_PATH, "logs.csv")

       
        os.makedirs(self.BASE_PATH, exist_ok=True)

        # Create empty files if not present
        for file in [self.BOOK_FILE, self.USER_FILE, self.ISSUED_FILE, self.LOG_FILE]:
            if not os.path.exists(file):
                open(file, "a").close()

    #LOG ACTION
    def log_action(self, msg):
        with open(self.LOG_FILE, "a") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {msg}\n")

    #ISSUE BOOK
    def issueBook(self):
        username = input('Enter username: ').strip()
        b_id = input('Enter Book ID to issue: ').strip()

       
        with open(self.USER_FILE) as f:
            lines = f.readlines()
            users = [line.strip().split(",")[1].strip().lower() for line in lines[1:] if line.strip()]
        if username.lower() not in users:
            print('\u274C User not found!')
            return

        with open(self.BOOK_FILE) as f:
            books = f.readlines()

        new_books = []
        issued = False
        header = ""
        if books and books[0].strip().startswith("BookID"):
            header = books[0]
            books = books[1:]

        for line in books:
            bid, title, author, avail = line.strip().split(",")
            if bid == b_id and avail.lower() == "yes":
                avail = "No"
                issued = True
            new_books.append(f"{bid},{title},{author},{avail}\n")

        with open(self.BOOK_FILE, 'w') as f:
            if header:
                f.write(header)
            f.writelines(new_books)

        if issued:
            with open(self.ISSUED_FILE, 'a') as f:
                f.write(f"{username},{b_id},{datetime.now().strftime('%Y-%m-%d')}\n")
            print('\U00002705Book issued successfully.')
            self.log_action(f'Book issued: {b_id} to {username}')
        else:
            print('Book not available or already issued.')

    #RETURN BOOK
    def returnBook(self):
        username = input('Enter username: ').strip()
        b_id = input('Enter Book ID to return: ').strip()

        if not os.path.exists(self.ISSUED_FILE):
            print('\u274C No issued book records found.')
            return

        with open(self.ISSUED_FILE) as f:
            issued = f.readlines()

        new_issued = []
        found = False
        for line in issued:
            u, bid, date_str = line.strip().split(",")
            if u.lower() == username.lower() and bid == b_id:
                found = True
                days = (datetime.now() - datetime.strptime(date_str, "%Y-%m-%d")).days
                fine = self.FINE if days > 7 else 0
                if fine > 0:
                    print(f'Book overdue! Fine: Rs.{fine}')
                self.log_action(f'Book returned: {b_id} by {username} (Fine Rs.{fine})')
            else:
                new_issued.append(line)

        with open(self.ISSUED_FILE, 'w') as f:
            f.writelines(new_issued)

        # Make book available again
        if os.path.exists(self.BOOK_FILE):
            with open(self.BOOK_FILE) as f:
                books = f.readlines()

            with open(self.BOOK_FILE, 'w') as f:
                for line in books:
                    bid, title, author, avail = line.strip().split(',')
                    if bid == b_id:
                        avail = 'Yes'
                    f.write(f"{bid},{title},{author},{avail}\n")

        if found:
            print('\U00002705 Book returned successfully.')
        else:
            print('\u274C  No record found for this user and book.')

    #VIEW LOGS 
    def viewLogs(self):
        if not os.path.exists(self.LOG_FILE) or os.path.getsize(self.LOG_FILE) == 0:
            print("No logs available.")
            return

        print("\n---- Library Logs ----")
        table = PrettyTable(["Timestamp", "Action"])
        with open(self.LOG_FILE) as f:
            for line in f:
                parts = line.strip().split(" - ", 1)
                if len(parts) == 2:
                    table.add_row(parts)
        print(table)

# # ---------------- MAIN MENU ----------------
# if __name__ == "__main__":
#     t = Transactions()
#     while True:
#         print("\n--- Transaction Menu ---")
#         print("1. Issue Book")
#         print("2. Return Book")
#         print("3. View Logs")
#         print("4. Exit")
#         choice = input("Enter your choice: ").strip()

#         if choice == '1':
#             t.issueBook()
#         elif choice == '2':
#             t.returnBook()
#         elif choice == '3':
#             t.viewLogs()
#         elif choice == '4':
#             print("Exiting system...")
#             break
#         else:
#             print("❌ Invalid choice! Try again.")
