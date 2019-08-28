# Problem Description: https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s

        mat = ['' for i in range(numRows)]
        curr, inc = 0, 1

        for word in s:
            if(curr == numRows):
                curr -= 2
                inc = -1
            elif(curr == -1):
                curr += 2
                inc = 1
            mat[curr] += word
            curr += inc

        return(''.join(mat))
