# Problem Description: Compute the last digit of F0+F1+···+Fn.

import doctest

f = [0, 1]


def fibsum(n):
    """Returns sum of last digits of n terms of Fibonacci series.

    Examples:
    >>> fibsum(3)
    4
    >>> fibsum(100)
    5
    """
    return (
        # (n // len(f)) * sum(f) +
        # As sum(f)%10==0, remove the above line.
        sum(f[:n % len(f) + 1])) % 10


if __name__ == "__main__":
    for i in range(2, 101):
        curr = (f[i-1] + f[i-2]) % 10
        if(curr == 0 and f[i-1] == 1):
            break
        f.append(curr)
    doctest.testmod()
    n = int(input())
    print(fibsum(n))
