"""
Ranges: Go over some examples of ranges


What we will cover?
    - create a range with start and end parameters
    - add step parameter
    - reverse a range
    - in, not in operators

Notes
    - Ranges are just list of consecutive
    numbers
    - The start number is included while
     the end number is not included.
        - Example
            range(start, end, step)
    - When using the reversed() function
    on a range, we get a range_iterable returned
    and we must turn that into a list
    to see our range reversed.
    - "in" operator determines if a element is
    in a list
    - "not in" operator determines if a element
    is not in a list


"""

nums = range(0,11)
print(nums)

# reverse a range
numss = list(reversed(range(0,11)))
print(numss)

print(1 in nums) # True, since it is in the range
print(2 not in nums) # False, since it is in the range

odd_nums = range(0,13,2)
print(odd_nums[1])