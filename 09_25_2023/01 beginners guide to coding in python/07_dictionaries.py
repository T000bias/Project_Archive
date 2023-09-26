"""
Dictionaries: Go over some examples of dictionaries

What will we cover?
    - Creating dictionaries
    - Accessing/modifying dictionary elements
    - Common dictionary operators

Notes

    - Based on key-value pairs.
    - Order doesn't matter as much as the keys
    - Syntax
        dictionary = {
            "key": "value"
        }

    - Similar to list we can use square brackets to access
    elements, but we need to specify the key to get the value.

    - To add elements we would specify the name of the key
    and assign it a value.
        - Example
            - dictionary["new_key"] = value
    - We can update values by specifying the value and update or
    convert it to a new value.

    - To check if a key is in a dictionary we can use the
    get function; Returns None if the value doesn't exist.
    If the item exists then the value gets returned.
        - Example
            dictionary.get("key")

    - Use keys() function to get all of the keys in the 
    dictioanry; Returns a tuple of all keys.

    - Use values() function to get all of the values from 
    dictionary.

    - The pop() function takes a key as the argument and removes
    both the key and value from the dictionary.

    - To clear all of the key-value pairs in a dictionary
    we can use the clear() function.

    - len() , min(), and max() functions work with dictionaries.
"""



inventory = {
    "Knife": 1, # This key-value pair is considered 1 item.
    "Health kit": 3,
    "wood": 5
}

print(inventory["wood"]) # Output = 5

# Inserting elements

inventory["keys"] = 4
print(inventory)

print(inventory.get("wood"))
print(inventory.get("gold"))

print(inventory.keys())
print(inventory.values())

print(inventory)
inventory.pop("keys")
print(inventory)