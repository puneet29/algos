class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        word_freq = {}
        for word in s:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
        for word in t:
            if word in word_freq:
                word_freq[word] -= 1
            else:
                return False
        return True if all(val == 0 for val in word_freq.values()) else False
