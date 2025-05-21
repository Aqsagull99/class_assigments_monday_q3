# %% [markdown]
# # Python Basics Practice (Chapters 1-9)
# ## Chapter 1: Introduction & Variables

# Introduction to Python

# Python is a high-level, interpreted programming language known for:
# - **Simple syntax** that emphasizes readability
# - **Versatility** (Web dev, data science, AI, automation, etc.)
# - **Rich ecosystem** of libraries (NumPy, Django, TensorFlow)
# - **Cross-platform compatibility** (Windows, macOS, Linux)

# Created by Guido van Rossum in 1991, Python supports both **object-oriented** and **procedural** programming paradigms. Its extensive standard library and beginner-friendly nature make it ideal for learners and professionals alike.

# %% [markdown]
# %% [code]
# Task 1: Create variables of all basic data types
name = "Alice"                  # string
age = 25                        # integer
height = 5.9                    # float
is_student = True               # boolean
fruits = ["apple", "banana"]    # list

print(f"Data Types:\nName: {type(name)}\nAge: {type(age)}\nHeight: {type(height)}")

# %% [markdown]
# ## Chapter 2: Operators & Keywords
# %% [code]
# Task 2: Demonstrate arithmetic and comparison operators
a, b = 10, 3
print(f"Addition: {a + b}")       # 13
print(f"Floor Division: {a // b}") # 3
print(f"Equal?: {a == b*3 + 1}")  # True

# %% [markdown]
# ## Chapter 3: Strings & Casting
# %% [code]
# Task 3: String manipulation and type conversion
text = "Python Exam"
print(text.upper())               # "PYTHON EXAM"
print(f"Length: {len(text)}")     # 11

num_str = "123"
print(int(num_str) * 2)          # 246 (casting)

# %% [markdown]
# ## Chapter 4: Control Flow
# %% [code]
# Task 4: If-else and loops
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")                   # Output: B
else:
    print("C")

# For loop with range
for i in range(1, 4):
    print(f"Count: {i}")         # Prints 1, 2, 3

# %% [markdown]
# ## Chapter 5: Lists, Tuples, Dictionaries
# %% [code]
# Task 5: Collection operations
colors = ["red", "green", "blue"]  # List (mutable)
colors[1] = "yellow"             # Update
print(colors)                    # ['red', 'yellow', 'blue']

point = (3, 4)                   # Tuple (immutable)
print(point[0])                  # 3

student = {"name": "Alice", "age": 25}  # Dictionary
print(student.get("age"))        # 25

# %% [markdown]
# ## Chapter 6: Sets
# %% [code]
# Task 6: Set operations
A = {1, 2, 3}
B = {3, 4, 5}
print(f"Union: {A | B}")         # {1, 2, 3, 4, 5}
print(f"Intersection: {A & B}")  # {3}

# %% [markdown]
# ## Chapter 7-8: Functions & Modules
# %% [code]
# Task 7: Create and import functions
def square(x):
    return x ** 2

print(square(4))                 # 16

# Importing math module
import math
print(f"Square root of 16: {math.sqrt(16)}")  # 4.0

# %% [markdown]
# ## Chapter 9: Exception Handling
# %% [code]
# Task 8: Handle division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")  # Custom message
finally:
    print("Execution complete.")


