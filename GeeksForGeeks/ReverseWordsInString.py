# Problem Description: https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0

t = int(input())

for _ in range(t):
    a = [x for x in input().split('.')]
    out = reversed(a)

    print('.'.join(out))
