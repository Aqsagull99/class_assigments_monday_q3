# Assignment: Python Operators Examples

# 1. Arithmetic Operators
x = 10
y = 3
print("Addition:", x + y)      # 13
print("Subtraction:", x - y)   # 7
print("Multiplication:", x * y) # 30
print("Division:", x / y)       # 3.333
print("Modulus:", x % y)        # 1
print("Exponentiation:", x ** y) # 1000
print("Floor Division:", x // y) # 3

# 2. Assignment Operators
a = 5
a += 2  # a = a + 2
print("a after +=:", a)  # 7
a *= 3  # a = a * 3
print("a after *=:", a)  # 21

a /= 7  # a = a / 7
print("a after /=:", a)  # 3.0

# 3. Comparison Operators
b = 10
c = 20
print("b == c:", b == c)  # False
print("b != c:", b != c)  # True
print("b > c:", b > c)    # False
print("b < c:", b < c)    # True

# 4. Logical Operators
is_sunny = True
is_warm = False
print("AND:", is_sunny and is_warm)  # False
print("OR:", is_sunny or is_warm)    # True
print("NOT:", not is_sunny)          # False

# 5. Identity Operators
d = [1, 2, 3]
e = [1, 2, 3]
f = d
print("d is e:", d is e)   # False (different objects)
print("d is f:", d is f)   # True (same object)
print("d is not e:", d is not e)  # True


# 6. Membership Operators
numbers = [1, 2, 3, 4, 5]
print("3 in numbers:", 3 in numbers)     # True
print("10 not in numbers:", 10 not in numbers)  # True


# 7. Bitwise Operators
g = 5  # 0101 in binary
h = 3  # 0011 in binary
print("Bitwise AND:", g & h)  # 0001 -> 1
print("Bitwise OR:", g | h)   # 0111 -> 7
print("Bitwise XOR:", g ^ h)  # 0110 -> 6
print("Bitwise NOT:", ~g)    # -(5+1) -> -6
print("Bitwise Left Shift:", g << 1)  # 1010 -> 10
print("Bitwise Right Shift:", g >> 1) # 0010 -> 2


