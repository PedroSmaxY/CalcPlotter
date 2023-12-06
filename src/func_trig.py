# Import necessary libraries
from sympy import symbols, diff, integrate, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# Use the Tkinter graphical interface to create the figure
matplotlib.use('TkAgg')

def trigonometric_function():
    clear_console()

    # Define the symbolic variable x
    x = symbols('x')

    # Loop to ensure the user inputs a valid trigonometric function
    while True:
        print("Enter the trigonometric function in terms of 'x' (e.g., sin(x))")
        try:
            # Try to convert the user input into a symbolic expression
            expr = sympify(input("\ny="))
            break
        except:
            # If an error occurs, display a message and continue the loop
            clear_console()
            print("Error: Invalid trigonometric function. Make sure to use the correct syntax.")
            continue

    # Calculate the derivative and integral of the function
    derivative = diff(expr, x)
    integral = integrate(expr, x)

    # Display information about the derivative and integral
    print(f"\nFunction's Derivative: {derivative}\n")
    print(f"Function's Integral: {integral} + c\n")

    # Convert the derivative expression into a numeric function
    derivative_func = lambdify(x, derivative, "numpy")

    # Generate x values for the plot
    x_vals = np.linspace(-100, 100, 10000)

    # Evaluate the expression to obtain corresponding y values
    y_vals_trig = [expr.subs(x, val) for val in x_vals]

    # Evaluate the derivative function at x values for the plot
    derivative_vals = derivative_func(x_vals)

    # Set the figure size
    plt.figure(figsize=(10, 5))

    # Define the plot for the trigonometric function
    plt.plot(x_vals, y_vals_trig, label="Trigonometric Function")
    # Define the plot for the derivative d(x)
    plt.plot(x_vals, derivative_vals, label="Derivative")

    # Set the width and thickness of the x and y axes
    plt.axvline(0, color='black', linewidth=1.5)
    plt.axhline(0, color='black', linewidth=1.5)

    # Set the title of the figure
    plt.title("Trigonometric Function Graph")
    # Set the names of the x and y axes
    plt.xlabel("x")
    plt.ylabel("y")

    # Set the view scale of the plot
    plt.xlim(-10, 10)
    plt.ylim(-5, 10)

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
    trigonometric_function()
else:
    from .clear_console import clear_console
