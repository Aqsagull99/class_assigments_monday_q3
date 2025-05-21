# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Function with default parameter
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # Uses default exponent 2
print(power(3, 3))   # Uses provided exponent 3