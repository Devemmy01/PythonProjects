principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principle amount: "))
    if principal < 0:
        print("Principal can't be less than Zero")
    else:
        break
    
while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Rate can't be less than zero")
    else:
        break
    
while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than Zero")
    else:
        break
    
total = principal * pow((1 + rate / 100), time)
print(f"Balance after {time} year(s) is ${total:.2f}")