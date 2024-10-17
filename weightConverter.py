# Convert kilogram to pound or pound to kilogram

weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds? (K or L): " ).upper()

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight in pounds is {round(weight)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight in Kilogram is {round(weight)} {unit}")
else:
    print(f"{unit} is not valid")