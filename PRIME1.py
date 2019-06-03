T = int(input())
for _ in range(T):
    l, u = map(int, input().split())
    composites = {}

    for i in range(2, u+1):
        if(i in composites):
            # This is a composite number
            for prime in composites[i]:
                if(prime+i in composites):
                    # Append the prime number to next multiple
                    composites[prime+i] += [prime]
                else:
                    # Add the prime number to next multiple
                    composites[prime+i] = [prime]
            del(composites[i])
        else:
            # This is a prime number
            if(i >= l):
                print(i)
            # Adds prime number at first composite index of the composites
            composites[i*i] = [i]

    print()
