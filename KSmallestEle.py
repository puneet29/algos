def insert(window, element, k):
    n = len(window)
    if(not n):
        window.append(element)
    elif(n == k):
        for i in range(k):
            if(window[i] > element):
                window.insert(i, element)
                break
        if(len(window) > k):
            del window[k]
    else:
        for i in range(n):
            if(window[i] > element):
                window.insert(i, element)
                return
        window.append(element)


t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    k = int(input())

    window = []
    for i in range(n):
        insert(window, arr[i], k)

    print(window[-1])
