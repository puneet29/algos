# Problem description: Compute the n-th Fibonacci number.

import doctest


def fibonacci(n):
    """Returns nth fibonacci number.

    Examples:
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(6)
    8
    >>> fibonacci(9)
    34
    """

    if(n <= 1):
        return n
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b


if __name__ == "__main__":
    doctest.testmod()
    n = int(input())
    print(fibonacci(n))
