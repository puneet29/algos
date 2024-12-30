class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        full_product = 1
        num_zeroes = 0
        for num in nums:
            if num == 0 and num_zeroes < 1:
                num_zeroes += 1
                continue
            full_product *= num
        res = []
        for num in nums:
            if num_zeroes > 1 or (num_zeroes == 1 and num != 0):
                res.append(0)
            elif num == 0:
                res.append(full_product)
            else:
                res.append(full_product/num)
        return res
