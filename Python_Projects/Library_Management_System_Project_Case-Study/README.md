📚 Library Management System Case-Study Project in Python

This project is a Library Management System developed using basic concept of Python and CSV files as the backend storage.
It helps manage books, users, and book issuing/returning operations without using any database nd Secure login with invisible password input.

✨ Project Features
Add New Books
Remove Book
View All Books
Add New users
View users
Remove users
Issue a Book
Return a Book
changed password
Data stored in CSV files
Handles invalid inputs
Simple and user-friendly menu

🗂 Technologies Used
python
CSV files for data storage
books.csv
users.csv
issue.csv
password.csv
 Libraries:
  - `getpass` (for invisible password input)
  - `emoji` (for adding emoji in UI)

This project simulates a real-world library where:
The librarian can add books with details like ID, name, author, email, phone number.
The system keeps track of registered users.
Books can be issued to users and stored in issue.csv.
When books are returned, the system updates the book stock and clears the issue record.
All data is permanently saved in CSV files so the system works without a database.

▶️ How to Run
Make sure Python is installed
Open terminal or VS Code
Run the program:
python main.py
Menu will appear → Choose the option (1–11)

📈 Learning Outcomes
By developing this project, I learned:
Working with CSV files (read/write)
File handling in Python
Menu-driven programs
Data management (add, update, delete)
Real-world Python application development
Problem-solving and debugging
