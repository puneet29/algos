class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalSum = nums[0]
        localSum = nums[0]
        for num in nums[1:]:
            localSum = max(num, num+localSum)
            globalSum = max(globalSum, localSum)
        return max(localSum, globalSum)
