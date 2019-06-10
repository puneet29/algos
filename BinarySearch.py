def binarySearch(arr, n, element):
    start, end = 0, n-1
    mid = (start+end)//2
    while(mid >= start and mid <= end and arr[mid] != element):
        if(arr[mid] > element):
            end = mid - 1
        elif(arr[mid] < element):
            start = mid + 1
        mid = (start+end)//2
    if(arr[mid] == element):
        return mid
    else:
        return -1


t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    ele = int(input())
    print(binarySearch(a, n, ele))
