# Write a function called chop that takes a list and modifies it, removing
# the first and last elements, and returns None. Then write a function called middle
# that takes a list and returns a new list that contains all but the first and last elements.

def chop(my_list):
    del my_list[0]
    del my_list[-1]
    return None


def middle(my_list):
    return my_list[1:-1]


numbers = [1, 2, 3, 4, 5]

chop(numbers)
print(numbers)

numbers = [1, 2, 3, 4, 5]

new_list = middle(numbers)
print(new_list)