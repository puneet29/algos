# Problem taken from CodeVita 8

def pattern(firststart, firstend, secondstart, secondend, n):
    arr = ['*' for i in range(n)]
    for i in range(firststart, firstend):
        arr.append(str(i)+'0')
    for i in range(secondstart, secondend):
        arr.append(str(i)+'0')
    arr.append(str(i+1))
    print(''.join(arr))


n = int(input())
mat = [[] for i in range(n)]
firststart = 1
firstend = n+1
secondstart = n*n+1
secondend = n*(n+1)

for i in range(n):
    pattern(firststart, firstend, secondstart, secondend, i*2)
    firststart = firstend
    firstend = firststart + n - i - 1
    secondend = secondstart - 1
    secondstart = secondend - n + i + 2
