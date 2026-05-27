name = "Jack"
age = 26
has_job = True
print("\n" + "=" * 40)
##### string slicing [start:end:step] #####
text = "Python Programming"
print("\nLength of text:", len(text))

print("\nBasic Slicing start to end")
print(f"text[0:6] = {text[0:6]}")
print(f"text[7:11] = {text[7:11]}")
print(f"text[7:18] = {text[7:18]}")

print("\nOmitting start or end")
print(f"text[:6] = {text[:6]}")     # From start to index 6
print(f"text[7:] = {text[7:]}")     # From index 7 to last
print(f"text[:] = {text[:]}")       # Copy whole string

print("\nNegative indices in slicing")
print(f"text[-11:] = {text[-11:]}")     # Last 11 characters
print(f"text[:-12] = {text[:-12]}")     # All except last 12
print(f"text[-11:-4] = {text[-11:-4]}") # Will print 'Program'

print("\nUsing step [start:end:step]")
print(f"text[::2] = {text[::2]}")       # Every 2nd char
print(f"text[::3] = {text[::3]}")       # Every 3rd char
print(f"text[0:6:2] = {text[0:6:2]}")       # Will print 'P' 't' 'o' from Python

print("\nReverse a string, step=-1")
print(f"text[::-1] = '{text[::-1]}'")

# Quotes inside strings
print("\nSingle quote: It\'s working!")     # needs \ to print ' or "" 
print("Double quote: She said \"Hello!\"")

# Carriage return (overwrites from beginning)
print("\nBefore", end="\r")     # After replaces Before but Before can be printed if used time.sleep(1)
print("After")

print("\nBackslash: C:\\Users\\Documents\\file.txt")      # Need \\ to print \
print(f"Row string: {r'C:\Users\Documents\file.txt'}")  # Treats it as raw string, doesn't interpret \n as newline

# Building a box
width = 30
print("+" + "-" * width + "+")
print("|" + " Welcome! ".center(width) + "|")
print("+" + "-" * width + "+")

# Width and alignment
print(f"Right align: '{name:>10}'")     # Right align: '     Jack'
print(f"Left align:  '{name:<10}'")     # Left align: 'Jack     '
print(f"Center:      '{name:^10}'")     # Center: '   Jack   '

# Thousands separator
big_num = 1234567
print(f"With commas: {big_num:,}")      # Will print 1,234,567

# Percentage
ratio = 0.856
print(f"Percentage: {ratio:.1%}")     # 85.6% for .0% = 86%, .2% = 85.60%, .4% = 85.6000%

print("\n3. .format() Method")
print("Name: {}, Age: {}".format(name, age))        # Name: Jack, Age: 26
print("Name: {0}, Age: {1}".format(name, age))      # Name: Jack, Age: 26
print("Name: {n}, Age: {a}".format(n=name, a=age))  # Name: Jack, Age: 26

# Formatting names
name = "jOHN DOE"
formatted = name.title()
print(f"\nFormatted name: {formatted}")

# casefold() - aggressive lowercase (for caseless comparisons)
german = "Straße"  # German word with ß
print(f"\nGerman word: '{german}'")
print(f"lower():    '{german.lower()}'")
print(f"casefold(): '{german.casefold()}'")  # ß becomes ss

print("\nPractical Example - Finding all occurrences:")
word = "Python"
start = 0
positions = []
while True:
    pos = text.find(word, start)
    if pos == -1:
        break
    positions.append(pos)
    start = pos + 1

print(f"'{word}' found at positions: {positions}")

words = ["Python", "is", "fun"]
print(f"Words: {words}")
print(f"' '.join(words):  '{' '.join(words)}'")
print(f"'-'.join(words):  '{'-'.join(words)}'")
print(f"''.join(words):   '{''.join(words)}'")

# Join numbers (must convert to strings first)
numbers = [1, 2, 3, 4, 5]
result = ", ".join(str(n) for n in numbers)
print(f"Numbers joined: '{result}'")