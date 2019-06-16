# Problem Description: https://practice.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair/0


t = int(input())

m = 1000000007
arr = [0, 1]
for i in range(2, 10**5+2):
    arr.append((arr[i-1] % m+arr[i-2] % m) % m)

for _ in range(t):
    n = int(input())
    print(arr[n+1])
