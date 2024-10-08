"""
app.py

This module provides a function to perform addition of two numbers.
"""

def addition(v1, v2):
    """
    Adds two numbers and returns the result.

    Args:
        v1 (int or float): The first number.
        v2 (int or float): The second number.

    Returns:
        int or float: The sum of v1 and v2.
    """
    return v1 + v2

# Example usage of the addition function
if __name__ == "__main__":
    result = addition(3, 5)  # Example values
    print(f"The result of addition is: {result}")

