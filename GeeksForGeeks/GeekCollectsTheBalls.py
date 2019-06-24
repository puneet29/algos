# Problem Description: https://practice.geeksforgeeks.org/problems/geek-collects-the-balls/0

t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    first = 0
    firstsum = 0
    second = 0
    secondsum = 0
    count = 0

    while(first < n and second < m):
        if(a[first] < b[second]):
            firstsum += a[first]
            first += 1
        elif(a[first] > b[second]):
            secondsum += b[second]
            second += 1
        else:
            count += secondsum if secondsum > firstsum else firstsum
            temp = a[first]
            count += temp
            first += 1
            second += 1
            firstsum, secondsum = 0, 0
            while(first < n and temp == a[first]):
                firstsum += a[first]
                first += 1
            while(second < m and temp == b[second]):
                secondsum += b[second]
                second += 1
            count += secondsum + firstsum
            firstsum, secondsum = 0, 0

    while(first < n):
        firstsum += a[first]
        first += 1
    while(second < m):
        secondsum += b[second]
        second += 1
    count += secondsum if secondsum > firstsum else firstsum
    print(count)
