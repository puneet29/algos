t = int(input())
for i in range(t):
    n = int(input())
    fact = 1
    for i in range(n-1):
        fact *= i+2
    print(fact)
