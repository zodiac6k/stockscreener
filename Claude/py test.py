# ====================================
# COMPREHENSIVE PYTHON PRACTICE SESSION
# ====================================

print("🐍 Welcome to Python Practice! 🐍\n")

# ====================================
# 1. VARIABLES AND DATA TYPES
# ====================================
print("=" * 50)
print("1. VARIABLES AND DATA TYPES")
print("=" * 50)

# Basic data types
name = "Alice"
age = 25
height = 5.7
is_student = True
favorite_numbers = [7, 13, 42]
person_info = {"name": "Bob", "age": 30}

print(f"String: {name} (type: {type(name).__name__})")
print(f"Integer: {age} (type: {type(age).__name__})")
print(f"Float: {height} (type: {type(height).__name__})")
print(f"Boolean: {is_student} (type: {type(is_student).__name__})")
print(f"List: {favorite_numbers} (type: {type(favorite_numbers).__name__})")
print(f"Dictionary: {person_info} (type: {type(person_info).__name__})")

# String operations
full_name = "John Doe"
print(f"\nString operations:")
print(f"Original: '{full_name}'")
print(f"Upper: '{full_name.upper()}'")
print(f"Lower: '{full_name.lower()}'")
print(f"Split: {full_name.split()}")
print(f"Length: {len(full_name)}")

# ====================================
# 2. LISTS AND LIST OPERATIONS
# ====================================
print("\n" + "=" * 50)
print("2. LISTS AND LIST OPERATIONS")
print("=" * 50)

# Creating and manipulating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]

print(f"Original fruits: {fruits}")
fruits.append("grape")
print(f"After append: {fruits}")
fruits.insert(1, "kiwi")
print(f"After insert: {fruits}")
fruits.remove("banana")
print(f"After remove: {fruits}")

# List comprehensions
squares = [x**2 for x in numbers]
even_numbers = [x for x in numbers if x % 2 == 0]
fruits_upper = [fruit.upper() for fruit in fruits]

print(f"\nList comprehensions:")
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")
print(f"Even numbers: {even_numbers}")
print(f"Fruits uppercase: {fruits_upper}")

# ====================================
# 3. DICTIONARIES
# ====================================
print("\n" + "=" * 50)
print("3. DICTIONARIES")
print("=" * 50)

# Creating and using dictionaries
student = {
    "name": "Emma",
    "age": 22,
    "courses": ["Python", "Math", "Physics"],
    "gpa": 3.8
}

print(f"Student info: {student}")
print(f"Name: {student['name']}")
print(f"Courses: {student['courses']}")

# Adding and updating
student["email"] = "emma@example.com"
student["age"] = 23
print(f"Updated student: {student}")

# Dictionary methods
print(f"\nDictionary methods:")
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# ====================================
# 4. FUNCTIONS
# ====================================
print("\n" + "=" * 50)
print("4. FUNCTIONS")
print("=" * 50)

# Basic function
def greet(name, greeting="Hello"):
    """Function with default parameter"""
    return f"{greeting}, {name}!"

# Function with multiple parameters
def calculate_area(shape, **kwargs):
    """Function with keyword arguments"""
    if shape == "rectangle":
        return kwargs["length"] * kwargs["width"]
    elif shape == "circle":
        return 3.14159 * kwargs["radius"] ** 2
    elif shape == "triangle":
        return 0.5 * kwargs["base"] * kwargs["height"]
    else:
        return "Unknown shape"

# Function with variable arguments
def sum_all(*args):
    """Function with variable arguments"""
    return sum(args)

# Testing functions
print(greet("Python"))
print(greet("World", "Hi"))
print(f"Rectangle area: {calculate_area('rectangle', length=5, width=3)}")
print(f"Circle area: {calculate_area('circle', radius=4):.2f}")
print(f"Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")

# ====================================
# 5. LOOPS AND ITERATIONS
# ====================================
print("\n" + "=" * 50)
print("5. LOOPS AND ITERATIONS")
print("=" * 50)

# For loops
print("For loop examples:")
for i in range(3):
    print(f"  Count: {i}")

for fruit in ["apple", "banana", "cherry"]:
    print(f"  I like {fruit}")

# While loop
print("\nWhile loop example:")
count = 0
while count < 3:
    print(f"  While count: {count}")
    count += 1

# Loop with enumerate
print("\nEnumerate example:")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"  {index}: {color}")

# ====================================
# 6. FILE OPERATIONS
# ====================================
print("\n" + "=" * 50)
print("6. FILE OPERATIONS")
print("=" * 50)

# Writing to file
filename = "python_practice.txt"
with open(filename, "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is a practice file.\n")
    file.write("Learning is fun!\n")

# Reading from file
with open(filename, "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Reading line by line
with open(filename, "r") as file:
    print("Reading line by line:")
    for line_num, line in enumerate(file, 1):
        print(f"  Line {line_num}: {line.strip()}")

# ====================================
# 7. ERROR HANDLING
# ====================================
print("\n" + "=" * 50)
print("7. ERROR HANDLING")
print("=" * 50)

def safe_divide(a, b):
    """Safe division with error handling"""
    try:
        result = a / b
        return f"{a} / {b} = {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Please provide numbers only!"
    except Exception as e:
        return f"Unexpected error: {e}"

def safe_access_list(lst, index):
    """Safe list access"""
    try:
        return f"Element at index {index}: {lst[index]}"
    except IndexError:
        return f"Error: Index {index} is out of range!"
    except Exception as e:
        return f"Error: {e}"

# Testing error hand