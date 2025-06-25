# Day 2 - String Slicing & Simple Calculator

# 🔹 Taking full name input
full_name = input("Enter your full name (first and last): ")

# 🔹 Slicing first and last name using string methods
# Assumes names are separated by a space
space_index = full_name.find(" ")
first_name = full_name[:space_index]
last_name = full_name[space_index+1:]

# 🔹 Displaying sliced names
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")

# 🔹 Taking two numeric inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# 🔹 Performing arithmetic operations
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

# 🔹 Displaying results with formatting
print(f"\nResults:")
print(f"{num1} + {num2} = {add}")
print(f"{num1} - {num2} = {sub}")
print(f"{num1} * {num2} = {mul}")
print(f"{num1} / {num2} = {div}")
