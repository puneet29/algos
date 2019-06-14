def get2D(a, n):
    return([a[i:i+n] for i in range(0, len(a), n)])


t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a = get2D(a, n)

    for i in range(n-1):
        for j in range(i, n):
            if(i != j):
                a[i][j], a[j][i] = a[j][i], a[i][j]

    for i in range(n):
        for j in range(n//2):
            a[i][j], a[i][n-1-j] = a[i][n-1-j], a[i][j]

    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")
    print()
