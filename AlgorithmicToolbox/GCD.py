# Problem Description: Compute the greatest common divisor of two positive
# integers.

import doctest


def GCD(a, b):
    """Returns Greatest common divisor(c) of a and b.

    Conditions: a%c==0 and b%c==0 and max(c) for all possible values of c.

    Examples:
    >>> GCD(28851538, 1183019)
    17657
    """

    for i in reversed(range(a+b+1)):
        if(not b % i and not a % i):
            return i
    return 1


def GCDfast(a, b):
    """Returns Greatest common divisor(c) of a and b. Uses the Euclid's algorithm:

    GCD(a, b) = GCD(a', b) = GCD(a, b'); where a' and b' are the remainders
    when a/b and b/a respectively.

    This is because a can be expressed as: a = a' + bx

    So, in order to divide a with c without any remainder,
    it must divide a' and b with c without any remainder.

    Conditions: a%c==0 and b%c==0 and max(c) for all possible values of c.

    Examples:
    >>> GCDfast(28851538, 1183019)
    17657
    """

    if(b == 0):
        return a
    return GCDfast(b, a % b)


if __name__ == "__main__":
    doctest.testmod()
    a, b = map(int, input().split())
    print(GCDfast(a, b))
