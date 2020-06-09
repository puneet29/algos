t = int(input())

for _ in range(t):
    s = input()
    status = [0 for i in range(len(s))]
    ans = 0

    for i in range(1, len(s)):
        if s[i-1] == 'x' and s[i] == 'y' and status[i-1:i+1] == [0, 0]:
            ans += 1
            status[i-1: i+1] = [1, 1]
        elif s[i-1] == 'y' and s[i] == 'x' and status[i-1:i+1] == [0, 0]:
            ans += 1
            status[i-1: i+1] = [1, 1]

    print(ans)
