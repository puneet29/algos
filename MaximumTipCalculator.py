t = int(input())

for _ in range(t):
    # x -> Threshold for Rahul, y -> Threshold for Ankit
    n, x, y = [int(x) for x in input().split()]

    # Tips for Rahul
    a = [int(x) for x in input().split()]

    # Tips for Ankit
    b = [int(x) for x in input().split()]

    diff = []

    for i in range(n):
        diff.append([abs(a[i]-b[i]), i])

    diff.sort(reverse=True)
    ans = 0

    for i in range(n):
        j = diff[i][1]
        if(x and y):
            if(a[j] > b[j]):
                ans += a[j]
                x -= 1
            else:
                ans += b[j]
                y -= 1
        elif(x):
            ans += a[j]
            x -= 1
        elif(y):
            ans += b[j]
            y -= 1
    print(ans)
