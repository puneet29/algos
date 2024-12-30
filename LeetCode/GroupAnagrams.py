from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        freq_dict = defaultdict(list)
        for element in strs:
            freq = [0] * 26
            for char in element:
                freq[ord(char)-ord("a")] += 1
            freq_dict[tuple(freq)].append(element)
        return list(freq_dict.values())
