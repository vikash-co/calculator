def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def calculator():
    print("Simple Calculator")
    print("Enter 'q' to quit.")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter the operator (+, -, *, /): ")
            if operator == 'q':
                break
            num2 = float(input("Enter the second number: "))

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator. Please try again.")
                continue

            print("Result:", result)
        except ValueError as e:
            print("Error:", e)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    calculator()