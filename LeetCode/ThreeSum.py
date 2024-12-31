from collections import defaultdict


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = set()
        all_nums = defaultdict(int)
        for num in nums:
            all_nums[num] += 1
        for curr_idx in range(len(nums)-2):
            first_num = nums[curr_idx]
            all_nums[first_num] -= 1
            for second_idx in range(curr_idx+1, len(nums)-1):
                second_num = nums[second_idx]
                third_num = - first_num - second_num
                if third_num < second_num:
                    # Because we want the search to be looking forward
                    # from second number (as array is sorted)
                    continue
                current_set = (first_num, second_num, third_num)
                if current_set in res:
                    continue
                all_nums[second_num] -= 1
                if third_num in all_nums and all_nums[third_num]>0:
                    res.add(current_set)
                all_nums[second_num] += 1
            all_nums[first_num] += 1
        return list(res)
