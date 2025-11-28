###2. Create a class Product with members as pid,pname,price and quantity .Add following 
# methods:
#e. Constructor (Support both parameterized and parameterless)
#f. Destructor
#g. ShowBook
#h. Add static member discount.
#i. Provide methods for applying discount on price of product.


class Product:
    discount = 0
    def __init__(self,pid = 0,pname = 0,price = 0,quantity = 0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def ShowProduct(self):
        return f'PID:{self.pid}\nPNAME:{self.pname}\nPRICE:{self.price}\nQUANTITY:{self.quantity}'
    
    def __del__(self):
        (f"Destructor is called")

    @staticmethod
    def set_discount(value):
        Product.discount = value
        print(f'Discount set to {Product.discount}%')



    
    def apply_discount(self):
        if Product.discount > 0:
            discounted_price = self.price - (self.price * Product.discount / 100)
            return f'Price after {Product.discount}% discount: {discounted_price}'
        else:
            return 'No discount applied.'

    # @staticmethod
    # def set_discount(value):
    #     Product.discount = value
    #     print(f'Discount set to {Product.discount}%')




p1 = Product(1, 'pen', 10, 2)
print(p1.ShowProduct())

Product.set_discount(10)  # Set 10% discount
print(p1.apply_discount())

#Parameterless constructor
p2 = Product() 
print(p2.ShowProduct())
print(p2.apply_discount())