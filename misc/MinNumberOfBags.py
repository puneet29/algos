# Problem: A salesman serves grocery items in packaged bags of varied sizes.
# The possible size of bags are {1, 5, 7, and 10} sizes. He wants to supply
# desired quantity using as less number of bags as possible irrespective of
# the size. Your objective is to help him find the minimum number of bags
# required to supply the given demand of grocery items.

t = int(input())

for _ in range(t):
    n = int(input())
    bags = [1, 5, 7, 10]
    no_bags = 4
    mat = [[0 for i in range(n+1)] for j in range(no_bags)]

    for i in range(no_bags):
        for j in range(1, n+1):
            if(i == 0):
                mat[i][j] = j
            else:
                if(j < bags[i]):
                    mat[i][j] = mat[i-1][j]
                else:
                    mat[i][j] = min(mat[i-1][j], 1+mat[i][j-bags[i]])

    print(mat[no_bags-1][n])
