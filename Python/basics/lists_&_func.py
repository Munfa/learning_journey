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