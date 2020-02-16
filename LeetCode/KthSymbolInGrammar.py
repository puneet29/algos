class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        a = '0'
        for i in range(1, N):
            b = ''
            for j in a:
                b += '01' if j == '0' else '10'
            a = b
        return a[K-1]
