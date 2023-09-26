"""
Conditionals: 
Explore conditionals in Python and how to add logic

What will we cover?
    - What are conditionals?
        - conditionals allow us to add logic to the code
        - we can choose which parts of the code to execute based
        on the outcome certain tests
        - Tests are typically comparing variables or testing the
        value of a single variable and always return true or false
    - If Statements?
        - Execute some statements if a text evaluates to True
        - Do nothing if the test evaluates to False
        - The test could check the value of a boolean variable
        or test equality between values.
    - elif statement
        - short for "else if"
        - provide an extra if statements
        - only executed if previous test(s) fail
        - can only come after if statement(s)
        - can chain together as many elif statments as you want
    - else statements
        - provides a failsafe
        - only executed if previous test(s) fail
        - can only come after if statement or elif statement
        - doesn't actually test anything, just executes code.
     - if statement variants
        - can nest if statements to add subsequent tests
        - can add multiple if statements in a row withou elif
        to perform all of the tests.
        - can add multiple testing conditions in if statements with
        or/and operators to test multiple conditions at once.
    
    Notes
        -
"""

# if/elif/else conditionals
key_press = 0
if key_press == 'right':
    print("going right")
elif key_press == 'left':
    print("going left")
else:
    print("going nowhere")


# Ternary Operator
"""
    - A shorter version of a if/elif/else statement.
    - This returns a result so the value is stored inside
    the variable
"""

command = "Move right" if key_press == "right" else "Move left"
print(command)

"""

If statements: Variants

What we will cover?
    - consecutive if statements
    - nested if statements
    - Adding multiple test cases in one if statement

Notes
    - consecutive if statements should be used if multiple
    conditions can be passed at the same time; good for
    debugging flow statements.
"""


num_lives = 3
health = 100

if health <= 0:
    # Nested if statements
    num_lives -= 1
    print("You died")
    if num_lives <= 0:
        print("game over")
elif health <= 10:
    print("warning")
else:
    print("no damage")

