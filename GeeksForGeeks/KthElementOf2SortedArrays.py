# Problem Description: https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array/0


def kthElement(a, n, b, m, k):
    if(k > (n+m) or k < 1):
        return -1
    if(n > m):
        return kthElement(b, m, a, n, k)
    if(n == 0):
        return b[k-1]
    if(k == 1):
        return min(a[0], b[0])

    i = min(n, k//2)
    j = min(m, k//2)

    if(a[i-1] > b[j-1]):
        return kthElement(a, n, b[j:], m-j, k-j)
    else:
        return kthElement(a[i:], n-i, b, m, k-i)


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, m, k = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]

        print(kthElement(a, n, b, m, k))
