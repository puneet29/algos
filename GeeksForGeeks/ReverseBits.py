# Problem Description: https://practice.geeksforgeeks.org/problems/reverse-bits/0

t = int(input())

for _ in range(t):
    n = int(input())
    bits = ''

    for i in range(32):
        bits += str(n % 2)
        n = n // 2

    bits = int(bits, 2)
    print(bits)
