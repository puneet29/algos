class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        max_length = 0
        for num in nums:
            if num - 1 not in nums_set:
                next_num = num + 1
                while next_num in nums_set:
                    next_num += 1
                max_length = max(next_num - num, max_length)
        return max_length
