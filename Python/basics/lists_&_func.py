# sort() - Sort in place (modifies original)
print("=== sort() - In-Place Sorting ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")

numbers.sort()
print(f"After sort(): {numbers}")

numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# sorted() - Returns new sorted list (original unchanged)
print("=== sorted() - Returns New List ===")
original = [3, 1, 4, 1, 5]
print(f"Original: {original}")

new_sorted = sorted(original)
print(f"sorted(original): {new_sorted}")
print(f"Original after sorted(): {original}")  # Unchanged!
print()

# ***** same with reverse() and reversed() ******

# List Comprehensions with Conditions (Filtering)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original: {numbers}")
print()

# Filter even numbers
print("=== Basic Filtering ===")
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

odds = [x for x in numbers if x % 2 != 0]
print(f"Odd numbers: {odds}")

# Single item tuple - REQUIRES trailing comma!
print("=== Single Item Tuples ===")
single = ("apple",)  # This is a tuple

# Only values > 25
big_values = {k: v for k, v in numbers.items() if v > 25}
print(f"Values > 25: {big_values}")
print()

# Remove specific keys
print("=== Remove Specific Keys ===")
original = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
remove_keys = {"b", "d"}
filtered = {k: v for k, v in original.items() if k not in remove_keys}
print(f"Original: {original}")
print(f"After removing {remove_keys}: {filtered}")

# Arbitrary Arguments: *args and **kwargs

# 1. *args - Accept any number of positional arguments
print("=== *args (Arbitrary Positional) ===")
def sum_all(*numbers):
    """Sum any number of arguments."""
    print(f"Received: {numbers}")  # It's a tuple!
    return sum(numbers)

print(f"Sum: {sum_all(1, 2, 3)}")
print(f"Sum: {sum_all(10, 20, 30, 40, 50)}")
print(f"Sum: {sum_all()}")  # Empty tuple OK
print()

# 2. **kwargs - Accept any number of keyword arguments
print("=== **kwargs (Arbitrary Keyword) ===")
def print_info(**info):
    """Print any keyword arguments passed."""
    print(f"Received: {info}")  # It's a dictionary!
    for key, value in info.items():
        print(f"  {key}: {value}")

print_info(name="Alice", age=25)
print_info(city="New York", country="USA", code="10001")
print()

# 4. Unpacking arguments
print("=== Unpacking Arguments ===")
def introduce(name, age, city):
    print(f"{name}, {age} years old, from {city}")

# Unpack list/tuple with *
person = ["Alice", 25, "Paris"]
introduce(*person)

# Unpack dict with **
person_dict = {"name": "Bob", "age": 30, "city": "London"}
introduce(**person_dict)

print("=== sorted() with Lambda ===")
words = ["banana", "pie", "Washington", "book"]

# Sort by length
by_length = sorted(words, key=lambda w: len(w))
print(f"By length: {by_length}")

print("=== map() with Lambda ===")
numbers = [1, 2, 3, 4, 5]

# Square each number
squares = list(map(lambda x: x ** 2, numbers))
print(f"Squares: {squares}")

# Greater than 5
big = list(filter(lambda x: x > 5, numbers))
print(f"Greater than 5: {big}")