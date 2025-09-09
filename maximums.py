def max_of_two(x, y):
    x = int(input("Enter a number:"))
    y = int(input("Enter another number:"))
    if x>y:
        return x
    else:
        return y


def max_of_three(x, y, z):
    x = int(input("Enter a number:"))
    y = int(input("Enter another number:"))
    z = int(input("Enter one more number:"))
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
