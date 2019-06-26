# Problem Description: https://practice.geeksforgeeks.org/problems/-minimum-number-of-coins/0

t = int(input())

for _ in range(t):
    n = int(input())
    denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
    denom = len(denominations)-1
    changes = []

    while(n > 0):
        if(denominations[denom] > n):
            denom -= 1
        else:
            changes.append(str(denominations[denom]))
            n -= denominations[denom]

    print(' '.join(changes))
