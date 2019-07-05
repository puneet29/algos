# Pattern: for 4
# 1
# 2*2
# 3*3*3
# 4*4*4*4
# 4*4*4*4
# 3*3*3
# 2*2
# 1

n = int(input())

if(n <= 0):
    print('Wrong Input')
else:
    for i in range(1, n+1):
        if(i == 0):
            print(i)
        else:
            print('*'.join([str(i) for j in range(i)]))
    for i in reversed(range(1, n+1)):
        if(i == 0):
            print(i)
        else:
            print('*'.join([str(i) for j in range(i)]))
