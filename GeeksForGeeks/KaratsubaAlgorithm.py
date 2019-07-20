# Problem Description: https://practice.geeksforgeeks.org/problems/karatsuba-algorithm/0

def karatsuba(a, b):
    if(a < 10 or b < 10):
        return a*b

    n = max(len(str(a)), len(str(b)))
    half = n // 2

    p = a // 10**(half)
    q = a % 10**(half)
    r = b // 10**(half)
    s = b % 10**(half)

    pr = karatsuba(p, r)
    qs = karatsuba(q, s)

    pqsumrs = karatsuba(p+q, r+s) - pr - qs

    prod = pr*10**(2*half) + pqsumrs*10**(half) + qs
    return prod


t = int(input())

for _ in range(t):
    a, b = [int(x, 2) for x in input().split()]
    print(karatsuba(a, b))
