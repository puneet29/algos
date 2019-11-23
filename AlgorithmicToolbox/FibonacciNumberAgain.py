# Problem Description: Compute the n-th Fibonacci number modulo m.

import doctest


def fibonaccimodulo(n, m):
    """Returns nth fibonacci number modulo m.

    Examples:
    >>> fibonaccimodulo(1, 239)
    1
    >>> fibonaccimodulo(115, 1000)
    885
    >>> fibonaccimodulo(2816213588, 30524)
    10249
    """

    f = [0, 1]
    reps = n+1
    for i in range(2, min(m**2, n+1)):
        curr = (f[i-1] + f[i-2]) % m
        if(i == n):
            return curr
        if(curr == 0 and f[i-1] == 1):
            reps = len(f)
            break
        f.append(curr)
    return f[n % reps]


if __name__ == "__main__":
    doctest.testmod()
    n, m = map(int, input().split())
    print(fibonaccimodulo(n, m))
