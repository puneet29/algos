# Problem taken from CodeVita 8

t = int(input())

for _ in range(t):
    p = input()
    s = input()
    d = {}
    res = ''

    for char in s:
        if(char in d):
            d[char] += 1
        else:
            d[char] = 1

    for char in p:
        if(char in d):
            while(d[char] != 0):
                res += char
                d[char] -= 1

    print(res)
