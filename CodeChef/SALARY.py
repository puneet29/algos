t = int(input())

for _ in range(t):
    n = int(input())
    w = [int(i) for i in input().split()]
    passes = 0
    wMin = min(w)
    done = False
    for i in w:
        if i == wMin and not done:
            done = True
        else:
            passes += i - wMin
    print(passes)
