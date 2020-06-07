t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    tot = 0

    for i in s:
        if i == '1':
            tot += 1

    print(sum(list(range(tot+1))))
