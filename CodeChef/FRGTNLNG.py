t = int(input())

for _ in range(t):
    n, k = [int(i) for i in input().split()]
    f = [i for i in input().split()]
    l, p = [], []
    for __ in range(k):
        temp = input().split()
        l.append(int(temp[0]))
        p += temp[1:]
    del temp
    p = set(p)

    for token in f:
        if token in p:
            print('YES', end=' ')
        else:
            print('NO', end=' ')
    print()
