# Basic multiple exception handling example

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Please enter numbers only")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Test cases
print("Test 1: Normal division")
divide_numbers(10, 2)  # Works fine

print("\nTest 2: Division by zero")
divide_numbers(5, 0)   # ZeroDivisionError

print("\nTest 3: Wrong data type")
divide_numbers("10", 2)  # TypeError

print("\nTest 4: Other error")
divide_numbers(10, '2')  # Will be caught by generic Exception