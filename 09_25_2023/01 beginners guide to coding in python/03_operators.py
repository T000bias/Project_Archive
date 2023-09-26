"""
What are operators?

- Operators enable us to perform operations on varaibles.
- A few operators modify a varialbe vaule
- Most operators produce a new result without 
modifying inputs.
- can be strung together, but always follow
order of operations.

Arithmetic Opearators

- Genearally used for numerical calculations
- Can be used to glue strings together
- produce a new numerical or string result
- addition: +
- substraction: - 
- multiplication: *
- division: /
- modulo: %
- floor division: //
- exponent: **

Assignment Operators

- used to assign values to variables.
- can be used in combination with arithmetic operators
- assignment operator: =
- +=. -=, *=, /=, %=, //=, **=

Comparsion Operators

- used to compare two values
- can be numerical string, or boolean variables
- ==, !=, >, >=, <, <=

Logical Operators

- used to test additional conditions
- typically used on booleans
- not, or, & and

other operators

- ternary operator: if else
- identity: is, is not
- membership: in, not in
- bitwise: &, |, ^, ~, <<, >>
"""

# Operators

# arithmetic operators
# health = 50
# print(health)
# health = health + 20 # adds to the current value
# print(health)

xPos = 5
# The original value will stay the same since we 
# are not saving the value.
# print(xPos % 2) # 5 % 2 (2*2=4) -> 5 - 4 = 1
# print(xPos // 2) # 5 // 2 -> 5 / = 2.5 (drop the decimal) = 2
# print(xPos //3)
# print(xPos ** 2)


# first_name = "rodney"
# last_name = "foster"
# print(first_name + " " + last_name)

# health = 50
# health += 20 # health = health + 20
# name = first_name
# name += " foster"
# print(name)
# print(health)
# assignment operators

# Operators 2
"""
What will we cover?

- comparison operators
- logical operators

Notes
- Strings are case-sensitive
- Based on the position in the Unicode standard, string values
have a value attached to them.
"""

# print(5 > 3)
# print(5 >= 5)
# print(3 == 3)
# print(3 != 1)
# print(5 == 5.0)
# print("a" == "A") # Strings are case-sensitive
# print("jfdl" > "kjfa")
# print(True == False)
# print(first_name == last_name)
# print(5 > False)
# print(5 > True) # True
# print(1 >= True)
# print(1 > True)

# logical operators

isGameOver = False
print(isGameOver)
isGameOver = not isGameOver # Reverses a boolean value
print(isGameOver)

health = 0
lives = 0
print(health <= 0 and lives <= 0)
print(health == 0 or lives > 1)