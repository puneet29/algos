# Problem Description: https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array/0

t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    k = int(input())

    mid = n//2
    ans = -1
    low, high = 0, n-1

    while(low <= high):
        if(a[mid] == k):
            ans = mid
            break
        if(a[mid] > a[low]):
            if(a[low] <= k and k < a[mid]):
                high = mid - 1
            else:
                low = mid + 1
        else:
            if(a[mid] < k and k <= a[high]):
                low = mid + 1
            else:
                high = mid - 1
        mid = (low + high) // 2
    print(ans)
