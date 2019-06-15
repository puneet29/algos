# Problem Description: https://practice.geeksforgeeks.org/problems/check-if-the-door-is-open-or-closed/0

def changeState(num):
    if(num == 1):
        return 0
    else:
        return 1


t = int(input())
for _ in range(t):
    n = int(input())
    state = [1] * (n + 1)
    for i in range(2, n+1):
        for j in range(i, n+1, i):
            state[j] = changeState(state[j])
    print(" ".join(map(str, state[1:])))
