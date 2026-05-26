##### Print the type of the variables #######
name = "Jack"
age = 26
has_job = True

print("Name type:", type(name))
print("Age type:", type(age))
print("Has_job type:", type(has_job).__name__)

##### Check Python reserved keywords ######
import keyword
print("\nPython reserved keywords:")
print(keyword.kwlist)
print(keyword.softkwlist)

##### Unpack from a list ######
numbers = [10, 20, 30, 40, 50]
first, *rest = numbers
print(f"\nFirst= {first}, Rest= {rest}")
first, *middle, last = numbers
print(f"First={first}, Middle={middle}, Last={last}")

#### Different number bases #####
binary = 0b1010      # Binary (base 2) = 10
octal = 0o17         # Octal (base 8) = 15
hexadecimal = 0xFF   # Hexadecimal (base 16) = 255

print(f"\nDifferent bases:")
print(f"Binary 0b1010 = {binary}")
print(f"Octal 0o17 = {octal}")
print(f"Hex 0xFF = {hexadecimal}")

##### Underscores for readability (Python 3.6+) #####
million = 1_000_000
credit_card = 1234_5678_9012_3456
print(f"\nWith underscores: {million:,}")

##### Float precision warning! #####
print("\nFloat precision issue:")
print(f"0.1 + 0.2 = {0.1 + 0.2}")  # Not exactly 0.3!
print(f"Expected: 0.3")

##### For precise decimals, use the decimal module #####
from decimal import Decimal
d1 = Decimal('0.1')
d2 = Decimal('0.2')
print(f"\nUsing Decimal: {d1} + {d2} = {d1 + d2}")

##### Complex numbers in Python #####
z1 = 3 + 4j
z2 = complex(2, -1)
z3 = 5j

print(f"\nz1= {z1}\nz2= {z2}\nz3= {z3}")
print(f"Real Part of z1= {z1.real}")
print(f"Imaginary part of z1= {z1.imag}")

##### divmod returns both quotient and remainder #####
quotient, remainder = divmod(17, 5)
print(f"\nQuotient= {quotient}, Remainder= {remainder}")