# Assignment: Control Flow & Loops in Python

Q1: Even or Odd Number
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

Q2: Grade Checker
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: Fail")

# # Q3: Sum of First N Numbers
n = int(input("Enter a number: "))
sum_n = sum(range(1, n+1))
print("Sum of first", n, "numbers is:", sum_n)

# Q4: Factorial Calculation
num = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print("Factorial of", num, "is:", factorial)

# Q5: Multiplication Table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Q6: Find Prime Number
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# Q7: Reverse a String
text = input("Enter a string: ")
print("Reversed string:", text[::-1])

# Q8: Count Vowels in a String
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)
print("Number of vowels:", vowel_count)

# Q9: Guessing Game
secret = 5
while True:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Try again!")

# Q10: Fibonacci Series
n = int(input("Enter the number of terms: "))
fib_series = [0, 1]
for _ in range(2, n):
    fib_series.append(fib_series[-1] + fib_series[-2])
print("Fibonacci series:", fib_series[:n])

