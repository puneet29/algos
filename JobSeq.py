# Problem Description: https://practice.geeksforgeeks.org/problems/job-sequencing-problem/0/

import operator

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    jobs = []
    for i in range(0, n*3, 3):
        job = [arr[i], arr[i+1], arr[i+2]]
        jobs.append(job)

    jobs.sort(key=operator.itemgetter(2), reverse=True)

    slots = [False] * n
    count = 0
    profit = 0

    for i in range(n):
        for j in reversed(range(min(n, jobs[i][1]))):
            if(not slots[j]):
                slots[j] = True
                profit += jobs[i][2]
                count += 1
                break

    print(count, profit)
