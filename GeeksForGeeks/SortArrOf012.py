# Problem Desciption: https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0

t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    mid = 0
    low = 0
    high = n-1

    while(mid <= high):
        if(a[mid] == 0):
            a[mid], a[low] = a[low], a[mid]
            low += 1
            mid += 1
        elif(a[mid] == 2):
            a[mid], a[high] = a[high], a[mid]
            high -= 1
        else:
            mid += 1

    print(" ".join([str(x) for x in a]))
