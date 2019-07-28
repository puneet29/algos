# Problem Description: https://practice.geeksforgeeks.org/problems/insertion-sort/1


def insert(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while(j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        insert(arr)

        for i in range(n):
            print(arr[i], end=" ")

        print()
