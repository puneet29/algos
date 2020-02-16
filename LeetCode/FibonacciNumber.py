class Solution:
    def fib(self, N: int) -> int:
        cache = {}

        def fibRecursion(N: int) -> int:
            if(N < 2):
                cache[N] = N
            if(N not in cache):
                cache[N] = fibRecursion(N-2) + fibRecursion(N-1)
            return cache[N]

        return fibRecursion(N)
