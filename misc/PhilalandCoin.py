# Problem taken from CodeVita

import math

t = int(input())

for _ in range(t):
    n = int(input())
    denominations = math.floor(math.log2(n)) + 1
    print(denominations)
