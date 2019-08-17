# Problem Description: https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) == 0):
            return 0
        start = 0
        max_len = 1
        used = set(s[0])

        for i in range(1, len(s)):
            if(s[i] in used):
                if(i-start > max_len):
                    max_len = i-start
                while(s[start] != s[i]):
                    used.remove(s[start])
                    start += 1
                used.remove(s[start])
                start += 1

            used.add(s[i])
        return max(max_len, len(s)-start)
