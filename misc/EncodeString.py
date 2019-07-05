# Problem: Encode the given decoded string, which has character and
# the number of times the character appeared.
# Input: a5br3
# Output: aaaaabrrr

s = input()

for i in range(len(s)):
    if((s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z')):
        print(s[i], end="")
    else:
        for j in range(int(s[i])-1):
            print(s[i-1], end="")
