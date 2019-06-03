T = int(input())
for _ in range(T):
    c, k, w = map(int, input().split())
    num = k // w
    if(num >= c):
        print("yes")
    else:
        print("no")
