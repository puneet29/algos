# Problem Description: https://practice.geeksforgeeks.org/problems/how-many-xs/0

t = int(input())

for _ in range(t):
    x = int(input())
    l, u = map(int, input().split())
    count = 0

    for i in range(l+1, u):
        count += str(i).count(str(x))

    print(count)