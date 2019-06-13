def countSubSeq(a):
    a_count = 0
    b_count = 0
    c_count = 0

    for i in range(len(s)):
        if(a[i] == 'a'):
            a_count = 1 + 2 * a_count
        elif(a[i] == 'b'):
            b_count = a_count + 2 * b_count
        elif(a[i] == 'c'):
            c_count = b_count + 2 * c_count
    return(c_count)


t = int(input())

for _ in range(t):
    s = input()
    print(countSubSeq(s))