# Import necessary libraries
from sympy import symbols, diff, integrate, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# Use the Tkinter graphical interface to create the figure
matplotlib.use('TkAgg')


def exponential_function():
    clear_console()

    # Define the symbolic variable x
    x = symbols('x')

    # Loop to ensure the user inputs a valid exponential function
    while True:
        print("Enter a function in terms of 'x' (e.g., x**2)")
        try:
            # Try to convert the user input into a symbolic expression
            function = sympify(input("\ny="))
            break
        except:
            clear_console()
            # If an error occurs, display a message and continue the loop
            print("Error: Invalid exponential function. Make sure to use the correct syntax.")
            continue

    # Calculate the derivative and integral of the function
    derivative = diff(function, x)
    integral = integrate(function, x)

    # Display information about the derivative and integral
    print(f"\nFunction's Derivative: {derivative}\n")
    print(f"Function's Integral: {integral} + c\n")

    # Convert the symbolic function to a function that can be numerically evaluated
    f = lambdify(x, function, "numpy")

    # Generate x values for the plot
    x_vals = np.linspace(-100, 100, 10000)

    # Evaluate the expression to obtain corresponding y values
    y_vals = f(x_vals)

    # Set the figure size
    plt.figure(figsize=(10, 5))

    # Define the plot for the function
    plt.plot(x_vals, y_vals, label="Function")
    # Define the plot for the derivative d(x)
    plt.plot(x_vals, [eval(str(derivative)) for x in x_vals], label="Derivative")

    # Set the width and thickness of the x and y axes
    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)

    # Set a title for the figure
    plt.title("Exponential Function Graph")
    # Set the names of the x and y axes
    plt.xlabel("x")
    plt.ylabel("y")

    # Set the view scale of the plot
    plt.xlim(-10, 10)
    plt.ylim(-5, 15)

    # Add legends for each function
    plt.legend()
    # Show the grid on the figure
    plt.grid(True)

    # Create the figure
    plt.show()
    input("\nPress ENTER to continue...")


# Run the main function if the script is executed as an independent program
if __name__ == "__main__":
    from clear_console import clear_console
    exponential_function()
else:
    from .clear_console import clear_console
