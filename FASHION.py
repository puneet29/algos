t = int(input())
for _ in range(t):
    n = int(input())
    men = [int(x) for x in input().split()]
    women = [int(x) for x in input().split()]
    men.sort()
    women.sort()
    res = 0
    for i in reversed(range(n)):
        res += men[i]*women[i]
    print(res)
