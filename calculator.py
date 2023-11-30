from input_handler import get_input
from operations import add, subtract, multiply, divide
from error_handler import handle_error

def main():
    try:
        num1, operator, num2 = get_input()
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            raise ValueError("Invalid operator.")
        print(f"The result is: {result}")
    except Exception as e:
        handle_error(e)

if __name__ == "__main__":
    main()
