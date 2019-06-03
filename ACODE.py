def decode(S, N):
    memo = [0 for i in range(N+1)]
    memo[N-1] = 1
    memo[N] = 1 if S[-1] != "0" else 0
    for i in reversed(range(N-1)):
        if(S[i] != "0"):
            if(int(S[i:i+2]) <= 26):
                memo[i] = memo[i+1] + memo[i+2]
            else:
                memo[i] = memo[i+1]
        else:
            if(int(S[i-1]) == 2 or int(S[i-1]) == 1):
                memo[i] = 0
            else:
                return(0)
    return(memo[0])


while(True):
    n = input()
    if(n == "0"):
        break
    print(decode(n, len(n)))
