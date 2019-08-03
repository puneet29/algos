# Needs optimization

def getPrimes(n):
    if(n < 2):
        return []
    if(n < 4):
        return [2, 3]
    primes = [2, 3]
    for i in range(5, int(n**(1/2)) + 1, 6):
        primes.append(i)
        primes.append(i+2)
    return primes


def getDivisors(n, primes):
    divisors = set([1, n])

    for i in range(len(primes)):
        prime = primes[i]
        if(n%prime == 0):
            divisors.add(prime)
            divisors.add(n//prime)
            for j in range(prime*2, n, prime):
                if(n%j==0):
                    divisors.add(j)
                    divisors.add(n//j)
                else:
                    break
    return(sorted(divisors))


if __name__ == "__main__":
    t = int(input())
    primes = getPrimes(10**(7.5))

    for _ in range(t):
        n = int(input())
        divisors = getDivisors(n, primes)

        for i in divisors:
            print(i, end=" ")
