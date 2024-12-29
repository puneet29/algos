class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff_cache = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in diff_cache:
                diff_cache[num] = i
            else:
                return [diff_cache[diff], i]
