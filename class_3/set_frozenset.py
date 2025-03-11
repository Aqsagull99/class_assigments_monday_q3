# Assignment: Sets & Frozensets in Python

# Q1: Create a Set and Perform Operations
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # Adding an element
my_set.remove(3)  # Removing an element
print("Updated Set:", my_set)

# Q2: Check if an Element Exists in a Set
print("Is 2 in set?", 2 in my_set)
print("Is 10 in set?", 10 in my_set)

# Q3: Perform Union, Intersection & Difference on Sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1 | set2)  # Union of sets
print("Intersection:", set1 & set2)  # Intersection of sets
print("Difference:", set1 - set2)  # Difference of sets

# Q4: Convert List to Set (Remove Duplicates)
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)  # Convert list to set
print("Unique Numbers:", unique_numbers)

# Q5: Create a Frozenset and Try to Modify It
frozen = frozenset([10, 20, 30, 40])
print("Frozenset:", frozen)
# frozen.add(50)  # This will raise an error because frozensets are immutable

# Q6: Check Subset and Superset
subset = {1, 2}
superset = {1, 2, 3, 4, 5}
print("Is subset a subset of superset?", subset.issubset(superset))
print("Is superset a superset of subset?", superset.issuperset(subset))

# Q7: Remove Element from Set Safely
set3 = {"a", "b", "c"}
set3.discard("b")  # Safely remove element without error
print("Updated Set:", set3)

# Q8: Find Symmetric Difference Between Two Sets
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print("Symmetric Difference:", setA ^ setB)

# Q9: Iterate Over a Set
char_set = {"x", "y", "z"}
for char in char_set:
    print("Character:", char)

# Q10: Convert String to Set (Unique Characters)
text = "banana"
unique_chars = set(text)
print("Unique Characters in String:", unique_chars)
