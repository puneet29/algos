# Problem Description: https://practice.geeksforgeeks.org/problems/concatenation-of-zig-zag-string-in-n-rows/0

t = int(input())

for _ in range(t):
    s = input()
    n = int(input())
    mat = [[] for i in range(n)]

    if(n == 1):
        print(s)
        continue

    row = 0
    sign = 1  # 1 for positive, 0 for negative

    for i in range(len(s)):
        if(row == 0):
            sign = 1
        elif(row == n-1):
            sign = -1
        mat[row].append(s[i])
        row += sign

    for i in mat:
        print(''.join(i), end='')
    print()
