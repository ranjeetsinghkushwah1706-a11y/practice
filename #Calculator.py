#Calculator
print("----- Simple Calculator -----")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Power (**)")

choice = input("Enter operation (+, -, *, /, %, **): ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == "+":
    print("Addition=", a + b)

elif choice == "-":
    print("subtraction =", a - b)

elif choice == "*":
    print("Multiplication =", a * b)

elif choice == "/":
    if b != 0:
        print("Division =", a / b)
    else:
        print("Error: Division by zero")

elif choice == "%":
    print("Reminder =", a % b)

elif choice == "**":
    print("Power =", a ** b)

else:
    print("Invalid operation")
