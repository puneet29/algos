# Problem Description: https://practice.geeksforgeeks.org/problems/recursively-remove-all-adjacent-duplicates/0/

def removeAdjacentDuplicates(s):
    a = s[:]
    i = 0
    while(i < len(a)-1):
        if(a[i] == a[i+1]):
            temp = a[i]
            while(i >= 0 and i < len(a) and a[i] == temp):
                del a[i]
        else:
            i += 1
    if(len(s) == len(a)):
        print(''.join(a))
    else:
        removeAdjacentDuplicates(a)


t = int(input())

for _ in range(t):
    s = list(input())
    removeAdjacentDuplicates(s)
