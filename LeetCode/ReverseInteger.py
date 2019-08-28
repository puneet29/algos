# Problem Description: https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        over = 2**(31)
        if(x < 0):
            res = -int(str(x)[::-1][:-1])
            return res if res >= -over else 0
        res = int(str(x)[::-1])
        return res if res < over else 0
