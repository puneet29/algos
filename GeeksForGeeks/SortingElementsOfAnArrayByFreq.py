# Problem Description: https://practice.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency/

t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    freq = {}
    ind = {}
    i = 1

    for num in a:
        if(num in freq):
            freq[num] += 1
        else:
            freq[num] = 1
        if(not num in ind):
            ind[num] = i
        i += 1

    d = []

    for key, val in freq.items():
        d.append([key, val])

    d.sort(key=lambda x: x[1], reverse=True)

    for i in d:
        for j in range(i[1]):
            print(i[0], end=" ")
    print()
