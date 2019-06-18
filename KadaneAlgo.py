# Problem Description: https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]

    local_sum = arr[0]
    global_sum = arr[0]

    for i in range(1, n):
        local_sum = max(arr[i], local_sum + arr[i])
        global_sum = max(local_sum, global_sum)

    print(global_sum)
