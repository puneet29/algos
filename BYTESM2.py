def findMax(memo, i, j, w):
    if(j == 0):
        return(max(memo[i+1][j], memo[i+1][j+1]))
    elif(j == w-1):
        return(max(memo[i+1][j], memo[i+1][j-1]))
    else:
        return(max(memo[i+1][j+1], memo[i+1][j], memo[i+1][j-1]))


for _ in range(int(input())):
    h, w = map(int, input().split())
    stones = []
    for row in range(h):
        stones.append([int(x) for x in input().split()])
    memo = [[0 for i in range(w)] for j in range(h)]
    memo[-1] = stones[-1]
    for row in reversed(range(h-1)):
        for col in range(w):
            memo[row][col] = stones[row][col] + findMax(memo, row, col, w)
    print(max(memo[0]))
