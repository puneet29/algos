# Problem Description: https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0

def permute(s, i=0):
    if(i == len(s)-1):
        return(''.join(s))

    else:
        res = ''
        for j in range(i, len(s)):
            s[i], s[j] = s[j], s[i]
            res += permute(s, i+1) + ' '
            s[i], s[j] = s[j], s[i]
        return res.rstrip()


t = int(input())

for _ in range(t):
    s = list(input())
    res = permute(s).split()
    res.sort()
    print(' '.join(res))
