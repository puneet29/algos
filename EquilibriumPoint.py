# Problem Description: https://practice.geeksforgeeks.org/problems/equilibrium-point/0/

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    res = -1
    lsum = 0
    rsum = sum(arr)

    for i in range(n):
        rsum -= arr[i]
        if(lsum == rsum):
            res = i+1
            break
        lsum += arr[i]
    print(res)
