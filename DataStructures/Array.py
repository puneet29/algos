import random
import time


def bubbleSort(arr):
    """
    Time complexity: O(n**2)
    """

    sortedArr = arr[:]
    for i in range(len(sortedArr) - 1):
        for j in range(i+1, len(sortedArr)):
            if sortedArr[i] > sortedArr[j]:
                sortedArr[i], sortedArr[j] = sortedArr[j], sortedArr[i]
    return sortedArr


def binarySearch(arr, item):
    """
    Time Complexity: O(log(n))
    """

    start, end = 0, len(arr)-1
    mid = start + ((end - start) // 2)
    while(end > start and arr[mid] != item):
        if arr[mid] < item:
            start = mid + 1
        else:
            end = mid - 1
        mid = start + ((end - start) // 2)
    if arr[mid] == item:
        return mid
    return -1


def mergeSort(arr):
    """
    Time Complexity: O(nlog(n))
    """

    def mergeHelper(arr1, arr2):
        if len(arr1) == 0:
            return arr2
        if len(arr2) == 0:
            return arr1
        res = []
        pointer1, pointer2 = 0, 0
        while(pointer1 < len(arr1) and pointer2 < len(arr2)):
            if arr1[pointer1] <= arr2[pointer2]:
                res.append(arr1[pointer1])
                pointer1 += 1
            else:
                res.append(arr2[pointer2])
                pointer2 += 1
        while(pointer1 < len(arr1)):
            res.append(arr1[pointer1])
            pointer1 += 1
        while(pointer2 < len(arr2)):
            res.append(arr2[pointer2])
            pointer2 += 1
        return res

    if (len(arr) <= 1):
        return arr
    firstHalf = mergeSort(arr[:len(arr)//2])
    secondHalf = mergeSort(arr[len(arr)//2:])
    return mergeHelper(firstHalf, secondHalf)


def quickSort(arr):
    """
    Time Complexity: O(n**2)
    If first element is the pivot to be taken and the array is sorted in decreasing order
    If pivot is the median of array everytime, then complexity reduces to O(nlog(n))
    """

    def partition(low, high, pivot, arr):
        if low >= high:
            return high
        while(low <= high):
            if (arr[low] > arr[pivot] and arr[high] <= arr[pivot]):
                arr[low], arr[high] = arr[high], arr[low]
            if arr[high] > arr[pivot]:
                high -= 1
            if arr[low] <= arr[pivot]:
                low += 1

        arr[pivot], arr[high] = arr[high], arr[pivot]
        return high

    if len(arr) <= 1:
        return arr

    pivotIndex = partition(0, len(arr) - 1, 0, arr)
    firstHalf = quickSort(arr[:pivotIndex])
    secondHalf = quickSort(arr[pivotIndex+1:])
    return firstHalf + [arr[pivotIndex]] + secondHalf


def insertionSort(arr):
    """
    Time Complexity: O(n**2)
    Concept of sorted sublist(initially of 1 len) and unsorted sublist(rest of the list)
    """
    for i in range(1, len(arr)):
        insertionElement = arr[i]
        j = i-1
        while(j >= 0 and arr[j] > insertionElement):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = insertionElement
    return arr


def selectionSort(arr):
    """
    Time complexity: O(n**2)
    Concept of sorted sublist(initially of 1 len) and unsorted sublist(rest of the list)
    """
    for i in range(len(arr)):
        minElementIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minElementIndex]:
                minElementIndex = j
        arr[i], arr[minElementIndex] = arr[minElementIndex], arr[i]
    return arr


if __name__ == '__main__':
    ARR_LENGTH = 10000

    arr = [random.randint(0, ARR_LENGTH*1000) for i in range(ARR_LENGTH)]
    print("Array representation:", arr, "\n")

    # Sorting ------------------------------------------------------------------------------
    start = time.time()
    bubbleSortArr = bubbleSort(arr)
    end = time.time()
    assert len(bubbleSortArr) == len(arr)
    print("Running Bubble Sort")
    # print("Sorted array:", bubbleSortArr)
    print(f"Took {end-start} seconds\n")

    start = time.time()
    mergeSortArr = mergeSort(arr)
    end = time.time()
    assert len(mergeSortArr) == len(arr)
    print("Running Merge Sort")
    # print("Sorted array:", mergeSortArr)
    print(f"Took {end-start} seconds\n")

    assert mergeSortArr[:] == bubbleSortArr[:]

    start = time.time()
    quickSortArr = quickSort(arr)
    end = time.time()
    assert len(quickSortArr) == len(arr)
    print("Running Quick Sort")
    # print("Sorted array:", quickSortArr)
    print(f"Took {end-start} seconds\n")

    assert quickSortArr[:] == bubbleSortArr[:]

    start = time.time()
    insertionSortArr = insertionSort(arr)
    end = time.time()
    assert len(insertionSortArr) == len(arr)
    print("Running Insertion Sort")
    # print("Sorted array:", insertionSortArr)
    print(f"Took {end-start} seconds\n")

    assert insertionSortArr[:] == bubbleSortArr[:]

    start = time.time()
    selectionSortArr = selectionSort(arr)
    end = time.time()
    assert len(selectionSortArr) == len(arr)
    print("Running Selection Sort")
    # print("Sorted array:", selectionSortArr)
    print(f"Took {end-start} seconds\n")

    assert selectionSortArr[:] == bubbleSortArr[:]

    # Searching ------------------------------------------------------------------------------
    searchElement = random.choice(arr)
    print(f"binarySearch(arr, {searchElement}):", binarySearch(mergeSortArr, searchElement))
    assert mergeSortArr[binarySearch(mergeSortArr, searchElement)] == searchElement

    print(f"binarySearch(arr, {ARR_LENGTH+1}):", binarySearch(mergeSortArr, ARR_LENGTH+1))
    assert binarySearch(mergeSortArr, ARR_LENGTH+1) == -1
