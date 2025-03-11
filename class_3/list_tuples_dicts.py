# Assignment: Lists, Tuples & Dictionary in Python

# Q1: Create a List and Perform Operations
my_list = [10, 20, 30, 40, 50]
my_list.append(60)  # Add an element
my_list.remove(30)  # Remove an element
print("Updated List:", my_list)

# Q2: Access Elements from a Tuple
tuple_data = ("Apple", "Banana", "Cherry", "Date")
print("First Element:", tuple_data[0])
print("Last Element:", tuple_data[-1])

# Q3: Modify a List Inside a Tuple
mixed_tuple = (1, 2, [3, 4, 5])
mixed_tuple[2].append(6)  # Modifying the list inside the tuple
print("Modified Tuple:", mixed_tuple)

# Q4: Dictionary Operations
student_info = {"name": "Aqsa", "age": 20, "course": "Python"}
print("Student Name:", student_info["name"])  # Accessing a value
student_info["age"] = 21  # Updating a value
student_info["grade"] = "A"  # Adding a new key-value pair
print("Updated Dictionary:", student_info)

# Q5: Iterate Over a List
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print("Number:", num)

# Q6: Check if Element Exists in Tuple
fruits = ("Mango", "Grapes", "Orange")
print("Mango is in tuple:", "Mango" in fruits)
print("Apple is in tuple:", "Apple" in fruits)

# Q7: Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}  # Merging dictionaries
print("Merged Dictionary:", merged_dict)

# Q8: Convert List to Tuple and Vice Versa
list_data = [10, 20, 30]
tuple_data = tuple(list_data)  # Convert list to tuple
new_list = list(tuple_data)  # Convert tuple back to list
print("Tuple:", tuple_data)
print("List:", new_list)

# Q9: Remove a Key from Dictionary
person = {"name": "Ali", "age": 25, "city": "Karachi"}
del person["age"]  # Removing key
print("Dictionary after deletion:", person)

# Q10: Sort a List and Convert it to Tuple
unsorted_list = [5, 2, 9, 1, 7]
sorted_list = sorted(unsorted_list)  # Sorting list
sorted_tuple = tuple(sorted_list)  # Converting to tuple
print("Sorted List:", sorted_list)
print("Sorted Tuple:", sorted_tuple)


