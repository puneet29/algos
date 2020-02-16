class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def util(n: int) -> int:
            if(n not in cache):
                if(n <= 2):
                    cache[n] = n
                else:
                    cache[n] = util(n-1) + util(n-2)
            return cache[n]

        return util(n)
