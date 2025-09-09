def roots(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return f"( )"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"({x})"
    elif discriminante > 0:
        x1 = (-b + discriminante**0.5) / (2*a)
        x2 = (-b - discriminante**0.5) / (2*a)
        return f"({x1}, {x2})"


def value_y(a, b, c, x):
    Y = a*x**2 + b*x + c
    return Y


def to_string(a, b, c):
    if a == 0 and b == 0:
        return f"f(x) = {c}"
    elif a == 0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"


def derivation(a, b, c):
    if a == 0 and b == 0:
        return f"f'(x) = 0"
    elif a == 0:
        return f"f'(x) = {b}"
    elif b == 0:
        return f"f'(x) = {2*a} * X"
    else:
        return f"f'(x) = {2*a} * X + {b}"

