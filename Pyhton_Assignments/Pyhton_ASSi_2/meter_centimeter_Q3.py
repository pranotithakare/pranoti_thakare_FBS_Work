###3. Convert distant given in feet and inches into meter and centimeter.

feet = int(input("Enter distance in feet: "))
inches = int(input("Enter distance in inches: "))
total_meters = (feet * 0.3048) + (inches * 0.0254)

meters = int(total_meters)
centimeters = (total_meters - meters) * 100

print(f"Distance is: {meters} meters and {centimeters:.2f} centimeters")
