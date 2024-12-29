class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        precedence = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev_precedence = -1
        noob_int = 0
        for c in reversed(s):
            curr_precedence = precedence[c]
            if curr_precedence >= prev_precedence:
                noob_int += curr_precedence
            else:
                noob_int -= curr_precedence
            prev_precedence = curr_precedence
        return noob_int
