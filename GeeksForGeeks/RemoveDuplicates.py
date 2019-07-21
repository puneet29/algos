# Problem Description: https://practice.geeksforgeeks.org/problems/remove-duplicates/0

def removeDuplicates(a):
    d = set()
    i = 0

    while(i < len(a)):
        if(a[i] in d):
            del a[i]
        else:
            d.add(a[i])
            i += 1
    print(''.join(a))


t = int(input())

for _ in range(t):
    a = list(input())
    removeDuplicates(a)
