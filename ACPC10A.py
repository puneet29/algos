a, b, c = map(int, input().split())
while(a != 0 or b != 0 or c != 0):
    if(b-a == c-b):
        v = b-a
        print("AP", c+v)
    elif(b/a == c/b):
        v = b/a
        print("GP", int(c*v))
    a, b, c = map(int, input().split())
