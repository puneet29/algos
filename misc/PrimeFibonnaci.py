# Problem taken from CodeVita


def checkPrime(n):
    if(n < 2):
        return False
    if(n < 4):
        return True
    if(not n % 2 or not n % 3):
        return False

    for i in range(5, int(n**(1/2))+1, 6):
        if(not n % i or not n % (i+2)):
            return False
    return True


def combinations(arr):
    out = []

    for i in range(len(arr)):
        for j in range(len(arr)):
            if(i == j):
                continue
            out.append(arr[i]+arr[j])
    return out


def fib(a, b, count):
    print(a, b, count)
    for _ in range(count-2):
        c = a+b
        a = b
        b = c
    print(b)


n1, n2 = [int(x) for x in input().split()]
primes = []

for i in range(n1, n2+1):
    if(checkPrime(i)):
        primes.append(i)

comb = set(map(int, combinations([str(x) for x in primes])))
comb = list(filter(checkPrime, comb))
fib(min(comb), max(comb), len(comb))
