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

