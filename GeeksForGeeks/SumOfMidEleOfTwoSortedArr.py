# Problem Description: https://practice.geeksforgeeks.org/problems/sum-of-middle-elements-of-two-sorted-arrays/0/


def median(arr, n):
    if(n % 2 == 0):
        return((arr[n//2] + arr[(n//2)-1])/2)
    else:
        return(arr[n//2])


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]

        mid = n//2
        ans = -1

        while(n > 2):
            m1 = median(a, n)
            m2 = median(b, n)
            if(m1 > m2):
                a = a[:mid + 1]
                if(n % 2 == 0):
                    b = b[mid - 1:]
                else:
                    b = b[mid:]
            else:
                if(n % 2 == 0):
                    a = a[mid - 1:]
                else:
                    a = a[mid:]
                b = b[:mid + 1]
            n = n // 2 + 1
            mid = n // 2

        if(n == 1):
            print(a[0] + b[0])
        elif(n == 2):
            print(max(a[0], b[0]) + min(a[1], b[1]))
        else:
            print(ans)
