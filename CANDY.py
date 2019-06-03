N = int(input())
while(N != -1):
    packs = []
    avg = 0
    for i in range(N):
        temp = int(input())
        packs.append(temp)
        avg += temp
    avg /= N
    pos = 0
    neg = 0
    if(int(avg) == avg):
        for candy in packs:
            temp = int(avg)-candy
            if(temp < 0):
                neg -= temp
            else:
                pos += temp
    else:
        pos = neg-1
    if(pos == neg):
        print(pos)
    else:
        print(-1)

    N = int(input())
