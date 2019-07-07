# Legendre polynomials using Bonnet's recursion formula

def legendre(n, x):
    dp = [1, x]
    if(n < 2):
        return(dp[n])
    else:
        for i in range(2, n+1):
            val = (2*i-1)*x*dp[i-1] - (i-1)*dp[i-2]
            val /= i
            dp.append(val)
        return dp[n]


m = int(input())

for _ in range(m):
    inp = input().split()
    n = int(inp[0])
    x = float(inp[1])

    print(round(legendre(n, x), 4))
