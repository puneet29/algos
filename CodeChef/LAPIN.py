t = int(input())

for _ in range(t):
    s = input()
    d = {}
    ans = 'YES'

    for i in range(len(s)//2):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1

    for i in range(len(s)//2):
        if s[-i-1] in d:
            d[s[-i-1]] -= 1
        else:
            ans = 'NO'
            break

    for i, j in d.items():
        if j != 0:
            ans = 'NO'
            break

    print(ans)
