import math

history_file = "history.txt"

def save_history(operation, result):
    with open(history_file, "a") as file:
        file.write(f"{operation} = {result}\n")

while True:
    print("\n===== ADVANCED PYTHON CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. View History")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == "9":
        print("Calculator Closed!")
        break

    elif choice == "8":
        try:
            with open(history_file, "r") as file:
                print("\n--- Calculation History ---")
                print(file.read())
        except FileNotFoundError:
            print("No history found.")
        continue

    elif choice == "7":
        num = float(input("Enter a number: "))
        result = math.sqrt(num)

        operation = f"√{num}"
        print("Result =", result)
        save_history(operation, result)

    elif choice in ["1", "2", "3", "4", "5", "6"]:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = num1 + num2
            operation = f"{num1} + {num2}"

        elif choice == "2":
            result = num1 - num2
            operation = f"{num1} - {num2}"

        elif choice == "3":
            result = num1 * num2
            operation = f"{num1} * {num2}"

        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero!")
                continue
            result = num1 / num2
            operation = f"{num1} / {num2}"

        elif choice == "5":
            result = num1 % num2
            operation = f"{num1} % {num2}"

        elif choice == "6":
            result = num1 ** num2
            operation = f"{num1} ^ {num2}"

        print("Result =", result)
        save_history(operation, result)

    else:
        print("Invalid Choice!")
