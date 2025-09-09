def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    x = int(input("Enter a number:"))
    y = int(input("Enter another number:"))
    if x>y:
        return x
    else:
        return y


def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    x = int(input("Enter a number:"))
    y = int(input("Enter another number:"))
    z = int(input("Enter one more number:"))
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
