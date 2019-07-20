# Problem Description: https://practice.geeksforgeeks.org/problems/inversion-of-array/0


def merge(arr, temp, left, mid, right):
    i = left
    j = mid+1
    k = left
    inv_count = 0

    while(i <= mid and j <= right):
        if(arr[i] <= arr[j]):
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1

    while(i <= mid):
        temp[k] = arr[i]
        k += 1
        i += 1

    while(j <= right):
        temp[k] = arr[j]
        k += 1
        j += 1

    for v in range(left, right+1):
        arr[v] = temp[v]

    return(inv_count)


def mergeSort(arr, temp, left, right):
    inv_count = 0

    if(left < right):
        mid = (left+right)//2
        inv_count = mergeSort(arr, temp, left, mid)
        inv_count += mergeSort(arr, temp, mid+1, right)
        inv_count += merge(arr, temp, left, mid, right)
    return(inv_count)


def getCount(arr, n):
    temp = [0]*n
    return(mergeSort(arr, temp, 0, n-1))


t = int(input())

for _ in range(t):
    n = int(input())
    c = [int(x) for x in input().split()]

    count = getCount(c, n)

    print(count)
