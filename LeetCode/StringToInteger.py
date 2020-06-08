class Solution:
    def myAtoi(self, str: str) -> int:
        nums = ["{}".format(i) for i in range(10)]
        negative = False
        ans = 0
        str = str.lstrip()
        if str.startswith('-'):
            negative = True
            str = str[1:]
        elif str.startswith('+'):
            str = str[1:]

        for i in str:
            if i in nums:
                ans = ans*10 + int(i)
            else:
                break

        if negative:
            ans = -ans

        if ans < -2**(31):
            ans = -2**(31)
        if ans >= 2**(31):
            ans = 2**(31) - 1

        return ans
