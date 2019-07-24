# Problem Description: https://practice.geeksforgeeks.org/problems/heap-sort/1

import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


def heapify(arr, n, i):
    '''
    :param arr: original array
    :param n: size of original array
    :param i: subtree rooted at ith index
    :return: 
    '''

    # Step 1: Get largest element among root, and its children
    largest = i
    l = 2*i+1
    r = l+1

    if(l < n and arr[i] < arr[l]):
        largest = l

    if(r < n and arr[largest] < arr[r]):
        largest = r

    # Step 2: If largest element root then end else:
    if(largest != i):
        # Step 3: Swap the largest children with root
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # Step 4: Heapify the changed heap after swap
        heapify(arr, n, largest)


def buildHeap(arr, n):
    '''
    :param arr: given array
    :param n: size of array
    :return: None
    '''

    # Step 1: Convert array to heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Step 2: Remove max element(root) and add to end
    for i in range(n-1, 0, -1):

        # Step 2.1: Swap the root with last element of array
        arr[i], arr[0] = arr[0], arr[i]

        # Step 2.2: Convert reduced array to heap
        heapify(arr, i, 0)


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        buildHeap(arr, n)
        print(*arr)
