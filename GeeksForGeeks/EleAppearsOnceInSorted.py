# Problem Description: https://practice.geeksforgeeks.org/problems/find-the-element-that-appears-once-in-sorted-array/0/


def search(arr, l, h):
    if(l > h):
        return
    if(l == h):
        return arr[l]

    mid = (l + h) // 2

    # Check the even and odd positioning of twin elements
    if(mid % 2 == 0):
        if(arr[mid] == arr[mid+1]):
            return(search(arr, mid+2, h))
        else:
            return(search(arr, l, mid))
    else:
        if(arr[mid] == arr[mid-1]):
            return(search(arr, mid+1, h))
        else:
            return(search(arr, l, mid-1))


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]

        print(search(a, 0, len(a)-1))
