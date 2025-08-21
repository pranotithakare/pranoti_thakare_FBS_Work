###Q3.Write a program to accept distance in km and convert it into meters and centimeters both.

km = float(input("enter distance in kilometers: "))
meters = km * 1000
centimeters = km * 100000
print(f'Distance in meters: ',meters)
print(f'Distance in centimeters: ',centimeters)