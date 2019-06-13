t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    diff = 999999

    for i in range(n):
        for j in range(i+1, n):
            if(abs(arr[j]-arr[i])<diff):
                diff = abs(arr[j]-arr[i])
    print(diff)