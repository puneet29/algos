t = int(input())

for _ in range(t):
    ts = int(input())

    if ts % 2 == 1:
        print(ts // 2)
        continue

    num = 1
    bints = '{0:b}'.format(ts)
    for i in reversed(bints):
        if i == '0':
            num += 1
        else:
            break

    temp = 2 ** num
    num = ts // temp

    print(num)
