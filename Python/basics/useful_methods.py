# ord() - character to ASCII/Unicode number
print("ord() - character to number:")
print(f"  ord('A') = {ord('A')}")   # 65
print(f"  ord('a') = {ord('a')}")   # 97
print(f"  ord('0') = {ord('0')}")   # 48

# chr() - number to character
print("\nchr() - number to character:")
print(f"  chr(65) = '{chr(65)}'")   # A
print(f"  chr(97) = '{chr(97)}'")   # a
print(f"  chr(128512) = '{chr(128512)}'")  # 😀

# With walrus operator - assign and use in same expression
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print(f"List has {count} elements (using walrus operator)")

# Only include squares greater than 10
# Calculate square once with walrus, use twice
large_squares = [square for x in numbers if (square := x**2) > 10]
print(f"Squares > 10: {large_squares}")


# Example: 201 in binary
n = 201
print(f"Example: {n} in 8-bit binary = {n:08b}")
print(f"  = 1×128 + 1×64 + 0×32 + 0×16 + 1×8 + 0×4 + 0×2 + 1×1")
print(f"  = 128 + 64 + 8 + 1 = {128 + 64 + 8 + 1}")

a = 12  # Binary: 1100
b = 10  # Binary: 1010

# Show binary representations
print("=== Binary Representations ===")
print(f"a = {a:2d}  →  binary: {bin(a):>6s}  →  {a:04b}")
print(f"b = {b:2d}  →  binary: {bin(b):>6s}  →  {b:04b}")

#Conditional formatting
print("=== Conditional Formatting ===")
items_count = 1
message = f"You have {items_count} item{'s' if items_count != 1 else ''}"
print(message)

# List comprehensions with ternary
print("=== In List Comprehensions ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(f"Numbers: {numbers}")
print(f"Labels:  {labels}")

# Classify temperatures
temps = [18, 22, 35, 12, 28]
comfort = ["cold" if t < 20 else "hot" if t > 30 else "nice" for t in temps]
print(f"Temps:   {temps}")
print(f"Comfort: {comfort}")