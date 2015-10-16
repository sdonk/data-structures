import string

from algodata.datastructures.basics import Stack

LETTERS_LOOKUP = {i + 10: string.ascii_lowercase[i] for i in range(26)}


def iterative_base_conversion(number, base):
    """
    Converts a number (base 10) into a string of any base using string
    """
    result = ""
    while number != 0:
        reminder = number % base
        number = number // base
        if 36 > reminder > 9:
            result += LETTERS_LOOKUP[reminder]
        else:
            result += str(reminder)
    # reverse the string
    return result[::-1]


def stack_iterative_base_conversion(number, base):
    """
    Converts a number (base 10) into a string of any base using a stack
    """
    stack = Stack()
    while number != 0:
        reminder = number % base
        number = number // base
        if 36 > reminder > 9:
            stack.push(LETTERS_LOOKUP[reminder])
        else:
            stack.push(reminder)
    # pop the elements out of the stack and return the result
    result = ""

    # the following code can be rewritten more elegantly using join and implementing __iter__ in the Stack
    # it's done in this way to demonstrate the underlying logic
    # see next function for a more Pythonic way
    while not stack.is_empty:
        result += str(stack.pop())
    return result


def list_iterative_base_conversion(number, base):
    """
    Converts a number (base 10) into a string of any base using a list
    """
    elements = []
    while number != 0:
        reminder = number % base
        number = number // base
        if 36 > reminder > 9:
            elements.append(LETTERS_LOOKUP[reminder])
        else:
            elements.append(str(reminder))
    return ''.join(reversed(elements))
