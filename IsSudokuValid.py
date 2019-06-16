def checkRow(a):
    vals = set()
    for i in range(9):
        if(a[i] in vals and a[i] != 0):
            return False
        else:
            vals.add(a[i])
    return True


def checkSudoku(mat):
    for i in range(9):
        if(not checkRow(mat[i])):
            return 0

    for i in range(9-1):
        for j in range(i, 9):
            if(i != j):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    for i in range(9):
        if(not checkRow(mat[i])):
            return 0

    return 1


t = int(input())

for _ in range(t):
    mat = [int(x) for x in input().split()]
    mat = [mat[i:i+9] for i in range(0, len(mat), 9)]

    print(checkSudoku(mat))
