def isPalindrome(a):
    temp = []

    for i in range(len(a)-1, -1):
        temp.append(a[i])

    if(temp == a):
        return True
    return False


def checkOpertations(a, n):
    i = 0
    j = n-1
    tot_op = 0

    while(j > i):
        if(a[i] == a[j]):
            i += 1
        elif(a[i] > a[j]):
            tot_op += 1
            a[j-1] += a[j]
            del a[j]
        else:
            tot_op += 1
            a[i+1] += a[i]
            del a[i]
        j -= 1

    return(tot_op)


t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    print(checkOpertations(a, n))
