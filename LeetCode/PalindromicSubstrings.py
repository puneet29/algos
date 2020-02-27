cache = {}
palcache = {}


class Solution:
    def countSubstrings(self, s: str) -> int:

        def checkPalindrome(s: str) -> bool:
            if(s not in palcache):
                palcache[s] = (s == (''.join(reversed(s))))
            return palcache[s]

        if(s not in cache):
            if(len(s) == 1):
                cache[s] = 1
            else:
                temp = self.countSubstrings(s[:-1])
                for i in range(len(s)):
                    temp += 1 if checkPalindrome(s[len(s)-1-i:]) else 0
                cache[s] = temp
        return cache[s]
