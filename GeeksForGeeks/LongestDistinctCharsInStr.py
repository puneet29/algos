# Problem Description: https://practice.geeksforgeeks.org/problems/longest-distinct-characters-in-string/0


def longestDistinct(a):
    d = set()
    start = 0
    longest = 0

    for i in range(len(a)):
        if(a[i] in d):
            longest = max(longest, i-start)
            while(start < i and a[i] != a[start]):
                d.remove(a[start])
                start += 1
            start += 1
        else:
            d.add(a[i])
    print(max(longest, i+1-start))


t = int(input())

for _ in range(t):
    a = input()
    longestDistinct(a)
