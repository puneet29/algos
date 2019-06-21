# Problem Description: https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

t = int(input())

for _ in range(t):
    n, s = map(int, input().split())
    arr = [int(x) for x in input().split()]

    window = []
    start = 0
    end = 0

    for i in range(n):
        window.append(arr[i])
        end = i
        while(sum(window) > s):
            del window[0]
            start += 1
        if(sum(window) == s):
            break

    if(sum(window) == s):
        print(start+1, end+1)
    else:
        print(-1)
