t = int(input())

for _ in range(t):
    s1 = input()
    s2 = input()
    delInd = 0
    temp = list(s1)

    for delInd in range(len(s2)):
        delChar = s2[delInd]
        n = len(temp)
        i = 0
        while(i < n):
            if(temp[i] == delChar):
                del temp[i]
                n = len(temp)
                continue
            i += 1

    print(''.join(temp))
