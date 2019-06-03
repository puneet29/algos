def F(X, N, C, val):
    prev = 0
    consumedC = 1
    for i in range(1, N):
        if(X[i]-X[prev] >= val):
            prev = i
            consumedC += 1
            if(consumedC >= C):
                return True
    return False


T = int(input())
for _ in range(T):
    N, C = map(int, input().split())
    X = []
    for i in range(N):
        X.append(int(input()))

    X.sort()

    end = X[N-1]
    start = 0

    while(end >= start):
        mid = (start + end)//2
        if(F(X, N, C, mid)):
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    print(ans)
