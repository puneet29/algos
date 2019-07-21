# Problem Description: https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays/0

'''
-----Logically correct approach-----
def merge(a, b, n, m):
    for i in range(n):
        # Step 1
        s = b[0]
        j = 0

        # Step 2
        while(a[i] > b[j]):
            b[j] = b[j+1]
            j += 1

        # Step 3
        if(j != 0):
            b[j-1] = a[i]
            a[i] = s
    print(' '.join(map(str, a+b)))
'''


def merge(a, b, n, m):
    i = 0
    j = 0

    while(i < n and j < m):
        if(a[i] < b[j]):
            print(a[i], end=' ')
            i += 1
        else:
            print(b[j], end=' ')
            j += 1
    while(i < n):
        print(a[i], end=' ')
        i += 1
    while(j < m):
        print(b[j], end=' ')
        j += 1
    print()


t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    merge(a, b, n, m)
