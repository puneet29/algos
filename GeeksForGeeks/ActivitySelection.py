# Problem Description: https://practice.geeksforgeeks.org/problems/activity-selection/0

t = int(input())

for _ in range(t):
    n = int(input())
    s = [int(x) for x in input().split()]
    f = [int(x) for x in input().split()]
    tasks = []

    for i in range(n):
        task = []
        task.append(s[i])
        task.append(f[i])
        tasks.append(task)

    tasks.sort(key=lambda x: x[1])

    count = 1
    i = 0
    for j in range(1, n):
        if(tasks[i][1] <= tasks[j][0]):
            count += 1
            i = j
    print(count)
