def findRev(num):
    temp = num
    rev = 0
    while(temp > 0):
        rev = rev * 10 + temp % 10
        temp = temp // 10
    return rev


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    revA = findRev(A)
    revB = findRev(B)
    print(findRev(revA + revB))
