# Problem Description: https://practice.geeksforgeeks.org/problems/minimize-the-heights/0

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    a = [int(x) for x in input().split()]

    if(n == 1):
        print(0)
        continue

    a.sort()

    ans = a[-1]-a[0]
    smallest = a[0] + k
    biggest = a[-1] - k

    if(smallest > biggest):
        smallest, biggest = biggest, smallest

    for i in range(1, n-1):
        upper = a[i] + k
        lower = a[i] - k
        if(lower > smallest or upper < biggest):
            continue
        if(biggest-lower <= upper-smallest):
            smallest = lower
        else:
            biggest = upper

    print(min(ans, biggest-smallest))
