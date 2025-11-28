#1. Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        print(f"Constructor called: ComplexNumber({self.real} + {self.imag}i)")

    def __del__(self):
        print(f"Destructor called: ComplexNumber({self.real} + {self.imag}i) destroyed")

    def __add__(self, other):
        # Overloading '+' operator
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return ComplexNumber(new_real, new_imag)

    def __sub__(self, other):
        # Overloading '-' operator
        new_real = self.real - other.real
        new_imag = self.imag - other.imag
        return ComplexNumber(new_real, new_imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

print("\nAddition:")
c3 = c1 + c2
print("Result:", c3)

print("\nSubtraction:")
c4 = c1 - c2
print("Result:", c4)


del c1
del c2
del c3
del c4
