# function returning two largest value in a list
def two_largest(lst):
    if len(lst) < 2:
        return "List must contain at least two elements."

    first = second = None

    for value in lst:
        if first is None or value >= first:
            second = first
            first = value
        elif second is None or value > second:
            second = value

    return (first, second)