t = int(input())

for _ in range(t):
    x, y, k, n = [int(i) for i in input().split()]

    lucky = 'UnluckyChef'
    if x <= y:
        lucky = 'LuckyChef'
    else:
        x = x - y
        for i in range(n):
            p, c = [int(i) for i in input().split()]
            if p >= x:
                if c <= k:
                    lucky = 'LuckyChef'
    print(lucky)
