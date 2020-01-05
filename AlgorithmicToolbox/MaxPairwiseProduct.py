# Problem description: Find the maximum product of two distinct numbers in a
# sequence of non-negative integers.

import doctest


def MaxPairwiseProduct(integers, n):
    """Return the maximum pair product from the list of integers of length n.

    Examples:
    >>> MaxPairwiseProduct([1,2,3], 3)
    6
    >>> MaxPairwiseProduct([7,5,14,2,8,8,10,1,2,3], 10)
    140
    """

    a, b = 0, 0
    for integer in integers:
        if(integer > a):
            b = a
            a = integer
            continue
        if(integer > b):
            b = integer
    return(a*b)


if __name__ == "__main__":
    doctest.testmod()
    n = int(input())
    integers = [int(i) for i in input().split()]
    print(MaxPairwiseProduct(integers, n))
