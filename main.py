from src.func_exp import exponential_function
from src.func_trig import trigonometric_function
from src.clear_console import clear_console

def calculator():
    while True:
        print("Welcome to the Graphing Calculator!")
        print("\nChoose an operation:\n")
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")
        print("5 - Exponential Function and Derivative/Integral Graph")
        print("6 - Trigonometric Function and Derivative/Integral Graph")
        print("0 - Exit\n")

        choice = input("Enter the number of the desired operation: ")

        if choice == '0':
            clear_console()
            print("Exiting the calculator. Goodbye!")
            break
        elif choice in ['1', '2', '3', '4']:
            clear_console()
            operation = int(choice)
            while True:
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    break
                except ValueError:
                    print("Error: Invalid input!")
                    input("Press ENTER to continue...")
                    clear_console()
                    continue

            if operation == 1:
                result = num1 + num2
                print(f"\nResult: {num1:.0f} + {num2:.0f} = {result:.0f}")
                input("\nPress ENTER to continue...")
                
            elif operation == 2:
                result = num1 - num2
                print(f"\nResult: {num1:.0f} - {num2:.0f} = {result:.0f}")
                input("\nPress ENTER to continue...")

            elif operation == 3:
                result = num1 * num2
                print(f"\nResult: {num1:.0f} x {num2:.0f} = {result:.0f}")
                input("\nPress ENTER to continue...")

            elif operation == 4:
                if num2 != 0:
                    result = num1 / num2
                    print(f"\nResult: {num1} / {num2} = {result:.2f}")
                    input("\nPress ENTER to continue...")
                else:
                    print("\nError: Division by zero!")
                    input("\nPress ENTER to continue...")

        elif choice == '5':
            exponential_function()

        elif choice == '6':
            trigonometric_function()
        else:
            clear_console()
            print("Invalid option. Please try again.")
            continue

        clear_console()

if __name__ == "__main__":
    calculator()
