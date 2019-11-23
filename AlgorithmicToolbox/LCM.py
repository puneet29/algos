# Problem Description: Compute the least common multiple of two positive
# integers.

import doctest


def GCD(a, b):
    """Returns Greatest common divisor(c) of a and b. Uses the Euclid's algorithm:

    GCD(a, b) = GCD(a', b) = GCD(a, b'); where a' and b' are the remainders
    when a/b and b/a respectively.

    This is because a can be expressed as: a = a' + bx

    So, in order to divide a with c without any remainder,
    it must divide a' and b with c without any remainder.

    Conditions: a%c==0 and b%c==0 and max(c) for all possible values of c.

    Examples:
    >>> GCD(28851538, 1183019)
    17657
    """

    if(b == 0):
        return a
    return GCD(b, a % b)


def LCM(a, b):
    """Returns the least common multiple(c) of a and b. Least common multiple
    is the smallest integer that is divisible by both a and b.

    Examples:
    >>> LCM(6, 8)
    24
    >>> LCM(28851538, 1183019)
    1933053046
    """

    h = GCD(a, b)
    if(b == 1 or a == 1 or h == 1):
        return(a*b)
    return(h * LCM(a//h, b//h))


if __name__ == "__main__":
    doctest.testmod()
    a, b = map(int, input().split())
    print(LCM(a, b))
