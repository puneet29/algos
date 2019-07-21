# Problem Description: https://practice.geeksforgeeks.org/problems/anagram/0

def checkAnagram(a, b):
    d = {}
    for i in a:
        if(i in d):
            d[i] += 1
        else:
            d[i] = 1

    for i in b:
        if(i in d):
            d[i] -= 1
        else:
            break

    for _, v in d.items():
        if(v != 0):
            return 'NO'
    return 'YES'


t = int(input())

for _ in range(t):
    a, b = [x for x in input().split()]

    print(checkAnagram(a, b))
