# Problem Description: Compute the last digit of
# Fm + Fm+1 + ··· + Fn.

import doctest

f = [0, 1]


def fibsumpartial(m, n):
    """Returns last digit of the partial sum of Fibonacci series between
    m (inclusive) and n (inclusive).

    Examples:
    >>> fibsumpartial(3, 7)
    1
    >>> fibsumpartial(10, 10)
    5
    """

    if(m > n):
        return -1
    if(len(f) > n):
        return sum(f[m:n+1]) % 10
    return (sum(f[m % len(f):]) +
            # (sum(f) % 10) * (n//len(f)-1) +
            # As sum(f)%10==0, remove above line
            sum(f[:n % len(f)+1])) % 10


if __name__ == "__main__":
    for i in range(2, 101):
        curr = (f[i-1] + f[i-2]) % 10
        if(curr == 0 and f[i-1] == 1):
            break
        f.append(curr)
    doctest.testmod()
    m, n = map(int, input().split())
    print(fibsumpartial(m, n))
