import math


class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if(N == 1 and K == 1):
            return 0
        prev = self.kthGrammar(N-1, math.ceil(K/2))
        if(prev == 0):
            return 1 if K % 2 == 0 else 0
        else:
            return 0 if K % 2 == 0 else 1
