from config import OPERATION_SYMBOLS

def get_input():
    """Get and validate user input."""
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    
    if operator not in OPERATION_SYMBOLS:
        raise ValueError("Invalid operator.")
    
    return num1, operator, num2
