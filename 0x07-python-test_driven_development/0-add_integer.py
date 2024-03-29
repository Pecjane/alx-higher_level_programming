c

"""
Addition module
"""


def add_integer(a, b=98):
    """
    Adds 2 integers.
    Args:
        a = first integer.
        b = second integer initialized to 98.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
