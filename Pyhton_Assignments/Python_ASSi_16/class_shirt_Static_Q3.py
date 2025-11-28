###3. Create a class Shirt with members as sid,sname,type(formal etc), price andsize(small,large etc) .
# Add following methods:
#j. Constructor (Support both parameterized and parameterless)
#k. Destructor
#l. ShowBook
#m. For each size of shirt price should change by 10%.
#(eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and xlarge=1300) Use static concept.

class Shirt:
    # Constructor (parameterized and parameterless)
    def __init__(self, sid=0, sname="Unknown", stype="casual", price=0.0, size="small"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.size = size
        self.price = price #self.calculate_price(price) 
        #print(f"Shirt {self.sname} created.")

    def __del__(self):
        print(f" destructor is called.")

    def ShowShirt(self):
        return f"SID:{self.sid}\nSNAME:{self.sname}\nTYPE:{self.stype}\nSIZE:{self.size}\nPRICE:{self.price}"


    def calculate_price(self, base_price):
        if self.size == "small":
            return base_price
        elif self.size == "medium":
            return base_price * 1.1
        elif self.size == "large":
            return base_price * 1.2
        elif self.size == "xlarge":
            return base_price * 1.3
        else:
            return base_price  # default if unknown size


    # def ShowShirt(self):
    #     return f"SID:{self.sid}\nSNAME:{self.sname}\nTYPE:{self.stype}\nSIZE:{self.size}\nPRICE:{self.price}"


shirt1 = Shirt(101, "Formal Shirt", "formal", 1000, "medium")
print(shirt1.ShowShirt())
print("          ")

shirt2 = Shirt(102, "Casual Shirt", "casual", 1000, "large")
print(shirt2.ShowShirt())
print("           ")

shirt3 = Shirt()  # Parameterless
print(shirt3.ShowShirt())
