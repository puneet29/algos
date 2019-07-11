# Problem Description: https://practice.geeksforgeeks.org/problems/merge-sort/1


def sortedMerge(a, b):
    apoint = bpoint = 0
    res = []

    while(apoint < len(a) and bpoint < len(b)):
        if(a[apoint] <= b[bpoint]):
            res.append(a[apoint])
            apoint += 1
        else:
            res.append(b[bpoint])
            bpoint += 1

    while(apoint < len(a)):
        res.append(a[apoint])
        apoint += 1

    while(bpoint < len(b)):
        res.append(b[bpoint])
        bpoint += 1

    return res


def mergeSortUtil(arr):
    n = len(arr)
    if(n < 0):
        return -1
    if(n == 1):
        return arr

    firsthalf = mergeSortUtil(arr[:n // 2])
    secondhalf = mergeSortUtil(arr[n // 2:])

    res = sortedMerge(firsthalf, secondhalf)
    return res


def mergeSort(arr):
    res = mergeSortUtil(arr)
    for i in range(len(arr)):
        arr[i] = res[i]


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        mergeSort(arr)
        for i in range(n):
            print(arr[i], end=" ")
        print()
