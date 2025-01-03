# Problem Description: https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        seen_set = set()
        start = 0
        max_length = 0

        for curr_idx, char in enumerate(s):
            if char in seen_set:
                max_length = max(curr_idx - start, max_length)
                while s[start] != char:
                    seen_set.remove(s[start])
                    start += 1
                start += 1
            seen_set.add(char)

        return max(max_length, len(s) - start)
