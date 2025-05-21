# Demonstrating file handling using the 'with' statement

# Example 1: Basic file writing with 'with'
with open('example.txt', 'w') as file:
    file.write("Hello, this is line 1.\n")
    file.write("This is line 2, written using with statement.\n")
    print("File written successfully!")

# The file is automatically closed here, even if an error occurs

# Example 2: Reading the file back
print("\nReading file contents:")
try:
    with open('example.txt', 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Error: File not found!")

# Example 3: Appending to file
with open('example.txt', 'a') as file:
    file.write("This line was appended later.\n")

# Example 4: Reading line by line
print("\nReading file line by line:")
with open('example.txt', 'r') as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")

# Benefits of 'with' statement:
# 1. Automatically closes the file
# 2. More concise code
# 3. Handles exceptions gracefully
# 4. Ensures proper resource cleanup