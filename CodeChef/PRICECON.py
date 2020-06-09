t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    p = [int(i) for i in input().split()]
    loss = 0

    for i in p:
        if i > k:
            loss += i - k

    print(loss)
