t = int(input())

for _ in range(t):
    n, k = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    mod = [(i+k) % 7 for i in c]
    wolves = 0

    for i in mod:
        if i == 0:
            wolves += 1
    print(wolves)
