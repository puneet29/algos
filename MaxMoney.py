t = int(input())

for _ in range(t):
    n, money = [int(x) for x in input().split()]

    if(n % 2):
        print(money*(n//2 + 1))
        continue
    else:
        print(money*(n//2))
