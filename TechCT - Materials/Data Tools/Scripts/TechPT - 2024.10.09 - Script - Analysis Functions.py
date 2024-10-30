import numpy as np
import argparse

# Data points (you can edit these values directly)
x_values = [2, 3, 4, 5, 6, 7, 8, 9]
y_values = [3, 4, 3, 4, 4, 5, 6, 6]

def calculate_slope_and_intercept():
    """
    Calculate the slope and intercept of the line that best fits the given data points.
    
    Prints:
    The slope and intercept of the best-fit line.
    """
    slope, intercept = np.polyfit(x_values, y_values, 1)
    print(f"The slope of the line is: {slope}")
    print(f"The intercept of the line is: {intercept}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate slope and intercept of a best-fit line.")
    parser.add_argument('function', type=str, help="The function to execute: 'slope_intercept'")

    args = parser.parse_args()

    if args.function == 'slope_intercept':
        calculate_slope_and_intercept()
    else:
        print("Unknown function. Available options: 'slope_intercept'")
