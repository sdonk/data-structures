import string

from datastructures import Stack

def iterative_base_conversion(N, K):
    """
    Converts the number N into a string of base K
    """
    # create dictionary lookup for reminder>=10
    LETTERS = {i+10: string.lowercase[i] for i in range(26)}
    result = ""
    while N>=K:
        reminder = N % K
        N = N / K
        if 36>reminder>9:
            result += LETTERS.get(reminder)
        else:
            result += str(reminder)
    # append the result of the last division
    result += str(N)
    # reverse the string
    return result[::-1]


def stack_iterative_base_conversion(N, K):
    """
    Converts the number N into a string of base K using a stack
    """
    # create dictionary lookup for reminder>=10
    LETTERS = {i+10: string.lowercase[i] for i in range(26)}
    stack = Stack()
    while N>=K:
        reminder = N % K
        N = N / K
        if 36>reminder>9:
            stack.push(LETTERS.get(reminder))
        else:
            stack.push(reminder)
    # append the result of the last division
    stack.push(str(N))
    # pop the elements out of the stack and return the result
    result = ""
    while not stack.is_empty:
        result += str(stack.pop())
    return result
