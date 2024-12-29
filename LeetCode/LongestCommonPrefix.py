class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        maximum_common_length = min(len(x) for x in strs)

        common_str = ""
        for i in range(maximum_common_length):
            if all(x[i] == strs[0][i] for x in strs):
                common_str += strs[0][i]
            else:
                break
        return common_str
