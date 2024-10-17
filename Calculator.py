# ask for a number
# ask for an operator
# ask for another number

# if the operator is +
    # print firstNumber + secondNumber
# else if the operator is -
    # print firstNumber - secondNumber
# if the operator is *
    # print firstNumber * secondNumber
# if the operator is /
    # print firstNumber / secondNumber
# else
    # print operator is not a valid operator


num1 = float(input("Enter a number: "))
operator = input("Enter an operator (+ - * /): ")
num2 = float(input("Enter another number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
else:
    print(f"{operator} is not a valid operator")
