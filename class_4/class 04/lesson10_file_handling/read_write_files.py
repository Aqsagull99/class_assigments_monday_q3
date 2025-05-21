# Writing to a file
with open('example.txt', 'w') as f:
    f.write("Hello, World!\n")
    f.write("This is a file handling example.\n")

# Reading from a file
with open('example.txt', 'r') as f:
    content = f.read()
    print("File content:")
    print(content)