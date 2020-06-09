n = int(input())

while(n != 0):
    arr = [int(i) for i in input().split()]
    newarr = []
    stack = []
    ans = 'yes'
    i = 0

    while(i < n and len(newarr) == 0):
        if arr[i] == 1:
            newarr.append(1)
        else:
            stack.append(arr[i])
        i += 1

    while(i < n):
        while(len(stack) > 0):
            if stack[-1] - 1 == newarr[-1]:
                newarr.append(stack.pop())
            else:
                break
        if arr[i] - 1 == newarr[-1]:
            newarr.append(arr[i])
        else:
            stack.append(arr[i])
        i += 1

    while(len(stack) > 0):
        if len(newarr) > 0:
            if stack[-1] - 1 == newarr[-1]:
                newarr.append(stack.pop())
            else:
                ans = 'no'
                break
        else:
            ans = 'no'
            break

    print(ans)

    n = int(input())
