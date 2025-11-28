###1. Create a class Book with members as bid,bname,price and author.Add following
#methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook
#d. Add static variable count and also maintain count of objects created.
class Book:
    count = 0
    def __init__(self,bid,bname,price = 0,author=0):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1
    def ShowBook(self):
        return f'BID:{self.bid}\nBNAME:{self.bname}\nPRICE:{self.price}\nAUTHOR:{self.author}'
    def __del__(self):
        print("destructor is called.")
    @staticmethod
    def countBook():
        print("Count of books : ",Book.count)
b1 = Book(1,'wings of fire',100,'abdul kalam')
print(b1.ShowBook())
Book.countBook()

