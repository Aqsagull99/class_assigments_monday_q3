# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Handling multiple exceptions
try:
    num = int("abc")
except ValueError:
    print("Invalid number format")
except Exception as e:
    print(f"An error occurred: {e}")