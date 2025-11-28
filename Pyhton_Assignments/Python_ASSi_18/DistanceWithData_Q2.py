# # 2. Create a class Distance with data members as km,m and cm and add following
# # methods :
# # a. Constructor
# # b. Destructor
# # c. Overload +,- operator

# class Distance:
#     def __init__(self,km,m,cm):
#         self.km = km
#         self.m = m
#         self.cm = cm
#         print(f"Constructor called: Distance({self.km} + {self.m} + {self.cm}i)")
#     def __del__(self):
#       print(f"destructor called: Distance({self.km} + {self.m} + {self.cm}i) destroyed.")  
    
#     def __add__(self,other):
#         #overloading '+' operator
#         new_km = self.km + other.km
#         new_m = self.m + other.m
#         new_cm = self.cm + other.cm
#         return Distance(new_km, new_m, new_cm)
    
#     def __sub__(self,other):
#         #overloading '-' operator
#         new_km = self.km - other.km
#         new_m = self.m - other.m
#         new_cm = self.cm - other.cm
#         return Distance(new_km, new_m, new_cm)
#     def __str__(self):
#         return f"{self.km} km + {self.m} m + {self.cm} cm"
    
# d1 = Distance(1,900,160)
# d2 = Distance(3,500,200)
# print("\nAddition:")
# d3 = d1 + d2
# print("result:",d3)

# #Sub
# print("\nSubtraction:")
# d4 = d1 - d2
# print("result:",d4)

# del d1
# del d2
# del d3
# del d4
    

    #________#################__________________

class Distance:
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm
        print(f"Constructor called: Distance({self.km} km + {self.m} m + {self.cm} cm)")

    def __del__(self):
        print(f"Destructor called: Distance({self.km} km + {self.m} m + {self.cm} cm) destroyed.")

    def normalize(self):
        # Convert cm to m
        self.m += self.cm // 100
        self.cm = self.cm % 100

        # Convert m to km
        self.km += self.m // 1000
        self.m = self.m % 1000

    def __add__(self, other):
        new_km = self.km + other.km
        new_m = self.m + other.m
        new_cm = self.cm + other.cm
        result = Distance(new_km, new_m, new_cm)
        result.normalize()
        return result

    def __sub__(self, other):
        # Convert all to centimeters
        total_self = self.km * 100000 + self.m * 100 + self.cm
        total_other = other.km * 100000 + other.m * 100 + other.cm
        diff = total_self - total_other

        if diff < 0:
            print("Warning: Distance cannot be negative. Returning 0.")
            return Distance(0, 0, 0)

        # Convert back
        km = diff // 100000
        diff %= 100000
        m = diff // 100
        cm = diff % 100

        return Distance(km, m, cm)

    def __str__(self):
        return f"{self.km} km + {self.m} m + {self.cm} cm"


# ✅ Test
d1 = Distance(1, 900, 160)
d2 = Distance(3, 500, 200)

print("\nAddition:")
d3 = d1 + d2
print("Result:", d3)

print("\nSubtraction:")
d4 = d1 - d2
print("Result:", d4)

del d1
del d2
del d3
del d4





