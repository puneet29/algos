# Problem Description: https://practice.geeksforgeeks.org/problems/quick-sort/1


def partition(arr, low, high):
    pivot = arr[high]
    # i points to the position of the pivot
    i = low

    for j in range(low, high):
        if(arr[j] <= pivot):
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    # swapping pivot to its sorted position
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quickSort(arr, low, high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        quickSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i], end=" ")
        print()
