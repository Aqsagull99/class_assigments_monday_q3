# Python Special Keywords Assignment

# Reserved keywords in Python represent built-in functionalities and are predefined by the 
# language. They help define the logic and flow of a program and ensure proper execution.
# Since these words have special meanings, they cannot be assigned to variables or used as identifiers.



# import keyword

# print(keyword.kwlist) # List of keywords



# import keyword
# print(len(keyword.kwlist))  # Total number of keywords count karega



# 1. Boolean & None Keywords

# True → Boolean True value ko represent karta hai. (e.g., x = True)

# False → Boolean False value ko represent karta hai. (e.g., y = False)

# None → Empty ya null value ko represent karta hai. (e.g., z = None)


# ✅ Allowed: Conditionals, assignments

# ❌ Not Allowed: Variable names (True = 5 ❌ Invalid)



# 2. Logical & Comparison Operators

# and → Dono conditions True honi chahiye (if a and b:)

# or → Koi ek condition True ho to chalega (if a or b:)

# not → Condition ka opposite karega (if not x:)

# is → Memory comparison ke liye (if a is b:)

# in → List ya sequence mein check karne ke liye (if x in my_list:)

# ✅ Allowed: Conditional statements
# ❌ Not Allowed: Variable names (is = 5 ❌ Invalid)



# 3. Control Flow (if-else & loops)

# if → Condition check karta hai (if x > 0:)

# elif → Else-if condition (elif x == 0:)

# else → Default block jab aur koi match na ho (else:)

# for → Looping ke liye (for i in range(5):)

# while → Looping jab tak condition True ho (while x < 10:)

# break → Loop ko forcefully stop karne ke liye (break)

# continue → Loop ke next iteration pe jump kare (continue)

# pass → Empty block ke liye (pass)

# ✅ Allowed: Loops, conditions
# ❌ Not Allowed: Standalone use (break bina loop ke ❌ Invalid)

# 4. Exception Handling

# try → Error-prone code likhne ke liye (try:)

# except → Jab error aaye toh is block mein aye (except ValueError:)

# finally → Try-except ke baad hamesha execute hoga (finally:)

# raise → Custom error generate karne ke liye (raise ValueError("Invalid"))

# assert → Condition check karne ke liye (assert x > 0)

# ✅ Allowed: Error handling
# ❌ Not Allowed: Outside try-except (except bina try ke ❌ Invalid)


# 5. Functions & Classes

# def → Function define karne ke liye (def my_func():)

# return → Function se value wapas bhejne ke liye (return x * 2)

# lambda → One-line function (lambda x: x * 2)

# class → Class banane ke liye (class Person:)

# ✅ Allowed: Function aur OOP programming
# ❌ Not Allowed: Outside function (return bina function ke ❌ Invalid)



# 6. Variable Scope & Memory Management

# global → Function ke andar global variable declare karne ke liye (global x)

# nonlocal → Nested function ke liye (nonlocal y)

# del → Variable ya object delete karne ke liye (del my_var)

# ✅ Allowed: Memory handling
# ❌ Not Allowed: Read-only objects par (del 5 ❌ Invalid)

# # 7. Importing Modules

# import → Module import karne ke liye (import math)

# from → Specific function import karne ke liye (from math import sqrt)

# as → Module ka alias banane ke liye (import numpy as np)

# with → Context manager ke liye (with open("file.txt") as f:)

# ✅ Allowed: Module handling
# ❌ Not Allowed: Standalone use (from bina import ke ❌ Invalid)

# 8. Pattern Matching (Python 3.10+)

# match → Switch-case jaisa (match x:)

# case → Condition define karne ke liye (case 1:)

# ✅ Allowed: Pattern matching
# ❌ Not Allowed: Old Python versions (3.9 ya older)

# 9. Async Programming (Python 3.5+)

# async → Asynchronous function define karne ke liye (async def my_func():)

# await → Async function call karne ke liye (await my_func())

# ✅ Allowed: Asynchronous programming
# ❌ Not Allowed: Normal functions mein (await bina async ke ❌ Invalid)

# Conclusion:

# Python has 35 special (reserved) keywords that cannot be used for any other purpose, such as variable or function names.
#  These keywords are an integral part of Python's syntax and structure.

