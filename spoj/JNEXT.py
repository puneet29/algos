# Problem Description: https://www.spoj.com/problems/JNEXT/

def just_next_partial(a, n):
    if n == 1:
        return -1

    largest = n-1

    for i in range(n-2, -1, -1):
        if a[i] >= a[largest]:
            largest = i
        if a[i] < a[largest]:
            break

    if largest == 0:
        return(-1)
    else:
        minEle = 10
        index = -1
        for x in range(i, n):
            if a[i] < a[x] and a[x] < minEle:
                minEle = a[x]
                index = x
        a[i], a[index] = a[index], a[i]
        a[largest:] = sorted(a[largest:])

        return(''.join(str(i) for i in a))


t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    print(just_next_partial(a, n))
