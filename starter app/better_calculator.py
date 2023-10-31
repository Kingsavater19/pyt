num1=float(input("Enter first number :"))
operator=input("Enter the Operator :")
num2=float(input("Enter second number :"))

if operator == "+":
    print(num1 + num2)
elif operator =="-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "**":
    print(num1 ** num2)
else:
    print("-----invalid Operator-----\n",operator ,"is not a vaild operator")