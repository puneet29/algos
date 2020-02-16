class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {}

        def helper(x: float, n: int) -> float:
            if(n not in cache):
                if(n == 0):
                    cache[n] = 1
                elif(n == 1):
                    cache[n] = x
                elif(n == -1):
                    cache[n] = 1/x
                elif(n % 2 == 0):
                    cache[n] = helper(x, n//2) * helper(x, n//2)
                else:
                    cache[n] = helper(x, n//2) * helper(x, n//2 + 1)
            return cache[n]

        return helper(x, n)
