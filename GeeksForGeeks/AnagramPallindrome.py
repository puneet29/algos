# Problem Description: https://practice.geeksforgeeks.org/problems/anagram-palindrome/0

def pallindromeAnagram(s):
    freq = set()

    for c in s:
        if(c in freq):
            freq.remove(c)
        else:
            freq.add(c)

    if(len(freq) == 0 or len(freq) == 1):
        return True
    return False


t = int(input())

for _ in range(t):
    s = input()

    if(pallindromeAnagram(s)):
        print('Yes')
    else:
        print('No')
