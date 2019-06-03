N = int(input())
while(N != 0):
    ans = 1
    for i in range(2, N+1):
        ans += i*i
    print(ans)
    N = int(input())
