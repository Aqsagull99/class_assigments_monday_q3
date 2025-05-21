import os

# Check if file exists
if os.path.exists('example.txt'):
    print("File exists")
    
    # Get file size
    size = os.path.getsize('example.txt')
    print(f"File size: {size} bytes")
else:
    print("File does not exist")