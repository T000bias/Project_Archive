# Collections

"""
Explore different collections types in Python

Whar are collections?

    - collections provide a way to store
    multiple values in a single variable.
    -Items in a collection are considered 
    elements.
    - Elements can also be collections
    - Usually come with additional functionality


Lists

    - List store 0 or more items at specific 
    indexes.
    - Access elements based on their index
    - Cannot access items at indexes that don't
    exists.
    - can contain multiple types of variables
    in Python.
    - Mutable


Tuples
    - Similar to lists
    - Access elements based on their index
    - Immutable

    
Dictionaries
    - Store key-value pairs at each index
    - each element is a tuple of key-value pair
    - access values based on key, not index
    - can also retrieve list of just keys or just values
    - Mutable

Ranges
    - Ranges represent lists of consecutie
    whole numbers, but don't have the functionality
    of lists
    - Specify start and end values
    - Can also specifiy step value
    - Wrap in reverse() function to 
    count backwards

"""


# Lists

"""
What will we cover?
    - Creating lists
    - Accessing /modifying list elements
    - common list operations
"""

inventory = ['sword', 'bread', 'boots']
# inventory = [0, 1, 2] indexes

inventory[0] = 'knife'
print(inventory)

print(len(inventory)) # 3: Always 1 more than max index
print(max(inventory)) # knife ? k > b
print(min(inventory)) # boots ? b < k

# add or delete items from a list

inventory.append("shows") # adds to the end of the list
print(inventory)

inventory.insert(0, 'fad') # specifies the index you add the item to
print(inventory)

# removing the last item
inventory.pop() # shows is removed
print(inventory)

inventory.append("shows")
inventory.pop(0) # index 0 item is removed
print(inventory)

inventory.insert(0,'fad')

del inventory[0]
print(inventory)

# clearing a list
lst = [1, 3, 4]
print(lst)

lst.clear()
print(lst)