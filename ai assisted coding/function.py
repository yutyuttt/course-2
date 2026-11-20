# function returning two largest value in a list
def two_largest(lst):
    if len(lst) < 2:
        return "List must contain at least two elements."

    first = second = None

    for number in lst:
        if first is None or number >= first:
            second = first
            first = number
        elif second is None or number > second:
            second = number

    return (first, second)