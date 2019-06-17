# Problem Description: https://practice.geeksforgeeks.org/problems/word-break-part-2/0


def wordBreak(s, dictionary, n, result, lasti=0, i=0):
    if(i >= n):
        return

    current = s[lasti:i+1]
    if(current in dictionary):
        temp = result + " " + current
        if(lasti == 0):
            temp = result + current

        if(i == n-1):
            print(temp, end=")")
            return

        wordBreak(s, dictionary, n, temp, i+1, i+1)

    wordBreak(s, dictionary, n, result, lasti, i+1)


t = int(input())

for _ in range(t):
    n = int(input())
    dictionary = [x for x in input().split()]
    s = input()

    result = "("
    wordBreak(s, dictionary, len(s), result)
    print()
