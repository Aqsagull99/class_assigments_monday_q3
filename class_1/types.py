### Python Data Types Assignment

# Data types in Python define the kind of value a variable can hold. Python provides several built-in data types,
#  which can be categorized into different groups.

#### 1. Numeric Types

# - int: Represents integers (10, -5)
  
#   x = 10
#   print(type(x))  # Output: <class 'int'>
  
# - float: Represents floating-point numbers (10.5, -3.14)
  
#   y = 10.5
#   print(type(y))  # Output: <class 'float'>


# Python mai complex number ko real_part + imaginary_part * j ki form mai likhte hain. Yahan j ek imaginary unit hai 
# jo -1 ka square root hota hai.

# - complex: Represents complex numbers (3 + 4j)
  
# z = 3 + 4j
# print(type(z))  # Output: <class 'complex'>


# z = 3 + 4j  # 3 real part hai, 4j imaginary part hai
# print(type(z))  # Output: <class 'complex'>

# # Real aur imaginary part ko alag print karna
# print(z.real)  # Output: 3.0
# print(z.imag)  # Output: 4.0 


# #### 2. Sequence Types

# - str: Represents a sequence of characters ('hello', "Python")
  
# s = "Hello"
# print(s)  # Output: <class 'str'>



# - list: An ordered, mutable collection of items [1, 2, 3]

#   lst = [1, 2, 3]
#   print(type(lst))  # Output: <class 'list'>

# - tuple: An ordered, immutable collection of items (1, 2, 3)

#   tup = (1, 2, 3)
#   print(type(tup))  # Output: <class 'tuple'>


# #### 3. Set Types

# - set: An unordered collection of unique elements always removes duplicates values {1, 2, 3}

#   s = {1, 2, 3}
#   print(type(s))  # Output: <class 'set'>

# - frozenset: An immutable version of a set

#   fs = frozenset([1, 2, 3])
#   print(type(fs))  # Output: <class 'frozenset'>


# #### 4. Mapping Type

# - dict: A collection of key-value pairs {'name': 'John', 'age': 25}

#   d = {'name': 'John', 'age': 25}
#   print(type(d))  # Output: <class 'dict'>


# #### 5. Boolean Type

# - bool: Represents True or False values

#   b = True
#   print(type(b))  # Output: <class 'bool'>


# #### 6. Binary Types

# - bytes: Immutable sequence of bytes

# bytes ek immutable sequence of bytes hoti hai, yani isko change nahi kiya ja sakta. Yeh binary
# data store karne ke liye use hoti hai,jaise images, files, ya network transmission.


# b = b"Hello"
# print(type(b))  # Output: <class 'bytes'>
# print(b)        # Output: b'Hello'
# print(b[0])     # Output: 72 (ASCII value of 'H')


# - bytearray: Mutable sequence of bytes

#   ba = bytearray(5)
#   print(type(ba))  # Output: <class 'bytearray'>

# - memoryview: Provides memory-efficient access to byte data

#   mv = memoryview(bytes(5))
#   print(type(mv))  # Output: <class 'memoryview'>



# #### 7. None Type

# - NoneType: Represents the absence of a value (None)

#   n = None
#   print(type(n))  # Output: <class 'NoneType'>


# ### Key Points:

# - Python is a dynamically typed language, meaning variables do not require explicit declaration of their type.
# - The type() function can be used to check the data type of a variable.
# - Type conversion (casting) allows changing data types using functions like int(), str(), float(), etc.







