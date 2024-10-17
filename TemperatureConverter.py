# Convert from Celcius to Fahrenheit or Fahrenheit to Celcius

unit = input("Enter the unit of the temperature. Celcius or Fahrenheit (C or F): ").upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((temp * 9)/ 5 + 32, 1)
    print(f"Your temperature in Fahrenheit is {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"Your temperature in Celcius is {temp}°C")
else:
    print(f"{unit} is not a valid unit")
