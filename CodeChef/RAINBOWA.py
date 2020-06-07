t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    seq = [-1 for i in range(1, 8)]
    curr = 1
    inc = 1
    i = 0

    while i < len(a):
        if a[i] == curr:
            while(i < len(a)):
                if a[i] != curr:
                    break
                if seq[a[i]-1] == -1:
                    seq[a[i]-1] = 1
                else:
                    seq[a[i]-1] += inc
                i += 1
            if curr == 7:
                inc = -1
            curr += inc
        else:
            break

    if seq[:-1] == [0 for i in range(6)]:
        print('yes')
    else:
        print('no')
