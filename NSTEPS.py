t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if(x == y):
        if(x % 2 == 0):
            print(x*2)
        else:
            print(x*2-1)
    elif(x-y == 2):
        if(x % 2 == 0):
            print(2*(x-1))
        else:
            print(2*x-3)
    else:
        print("No Number")
