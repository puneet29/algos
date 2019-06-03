# This algorithm uses sparse dictionary of Python

import collections
T = int(input())
for _ in range(T):
    l, u = map(int, input().split())
    composites = collections.defaultdict(list)

    for i in range(2, u+1):
        if(i in composites):
            # This is a composite number
            for prime in composites[i]:
                # Append the prime number to next multiple
                composites[prime+i].append(prime)

            del(composites[i])
        else:
            # This is a prime number
            if(i >= l):
                print(i)
            # Adds prime number at first composite index of the composites
            composites[i*i] = [i]

    print()
