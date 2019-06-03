def palindrome(A, size):
    MAT = [[0 for j in range(size)] for i in range(size)]
    i = 0
    diff = 1
    while(diff <= size - 1):
        j = i + diff
        if(A[i] == A[j]):
            MAT[i][j] = MAT[i+1][j-1]
        else:
            MAT[i][j] = min(MAT[i][j-1], MAT[i+1][j]) + 1

        if(j == size - 1):
            i = 0
            diff += 1
        else:
            i += 1
    return(MAT[0][size-1])


for _ in range(int(input())):
    S = str(input())
    print(palindrome(S, len(S)))
