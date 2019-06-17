# Problem Description: https://practice.geeksforgeeks.org/problems/word-break/0

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [x for x in input().split()]
    word = input()

    lasti = 0
    for i in range(len(word)):
        if(word[lasti:i+1] in arr):
            lasti = i+1

    if(lasti == len(word)):
        print(1)
    else:
        print(0)
