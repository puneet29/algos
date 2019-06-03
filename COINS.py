def maxCoins(n, memo={}):
    if(n <= 4):
        memo[n] = n
        return (n)
    if(n in memo):
        return (memo[n])
    else:
        memo[n] = max(n, maxCoins(n//2, memo) +
                      maxCoins(n//3, memo)+maxCoins(n//4, memo))
        return (memo[n])


try:
    while(True):
        n = int(input())
        print(maxCoins(n))
except Exception:
    pass
