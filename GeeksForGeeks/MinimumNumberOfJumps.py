# Problem Description: https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps/0

# def MinimumJumps(arr, n):
#     jumps = [0]*n

#     for i in reversed(range(n)):
#         if(arr[i] == 0):
#             jumps[i] = float('inf')
#         elif(arr[i] >= n-i-1):
#             jumps[i] = 1
#         else:
#             minJump = float('inf')
#             for j in range(i+1, arr[i]+i+1):
#                 if(jumps[j] < minJump):
#                     minJump = jumps[j]
#             if(minJump != float('inf')):
#                 jumps[i] = minJump + 1
#             else:
#                 jumps[i] = minJump
#     if(jumps[0] == float('inf')):
#         return(-1)
#     else:
#         return(jumps[0])


def MinimumJumps(arr, n):

    if(n < 1 or arr[0] == 0):
        return(-1)

    maxReach = arr[0]
    step = arr[0]
    jumps = 1

    for i in range(1, n):
        if(i == n-1):
            return(jumps)
        else:
            maxReach = max(maxReach, i + arr[i])

            step -= 1

            if(step == 0):
                jumps += 1

                if(i >= maxReach):
                    return(-1)

                step = maxReach - i
    return(-1)


t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    print(MinimumJumps(a, n))
