num_lives = 5
# we can convert an int/float to a string with
# the str() function
str_num_lives = str(num_lives)
print(type(num_lives))
print(type(str_num_lives))

# converting a boolean value

# Everything in python evaluates to true?
# Everything except the value of 0 and False is True.

print(bool(0)) # should be false
print(bool(1)) # should be true
print(bool(2)) # should be true
print(bool("dfjklas;fj")) # should be true
pritn(bool("False")) # should be True even though we are evaluating a boolena string
print(bool(True)) # should be true
print(bool(False)) # should be false

# Converting to integers

# print(int("fjkalds;")) # ValueError
print(int("5")) # should be integer 5; only works with strings that are whole numbers
print(int(1.2)) # should be integer 1
print(float("5.0")) # should be 5.0; only works with strings that are floats


# converting to floats
print(float("1")) #will add the .0 to the number
print(float(0.5)) # standard conversion
print(float(False)) # 0.0; since False is 0, 0.0 would be the float equivalent
print(float(True)) # 1.0; since True is 1, 1.0 would be the float equivalent