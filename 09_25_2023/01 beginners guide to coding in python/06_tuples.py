"""
Tuples: Go over some examples of tuples

What will we create?
    - Creating tuples
    - Accessing tuple elements
    - Common tuple operations
    - Compare to lists

Notes
    - Cannot be changed; usually used just
    to store values.
    - Index based
    - We can modify the tuple itself, but not
    the elements inside of it.
    - .count returns how many elements of that
    type are in the tuple; case-sensitive.
    - .index returns the lowest index of a 
    specific item.
"""

item = ("health kit", 4, True)
print(item[0])
print(item[1])
# We can modify the tuple itself, but not the elements inside of it.
item = ("Knife", "knife", 1)
print(item)

print(item.count("Knife"))
print(item.index(1))
print(len(item))
# print(max(item))
# print(min(item))