class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def sortedMerge(a: List[int], b: List[int]) -> List[int]:
            a1, b1 = 0, 0
            res = []
            while(a1 < len(a) and b1 < len(b)):
                if(a[a1] <= b[b1]):
                    res.append(a[a1])
                    a1 += 1
                else:
                    res.append(b[b1])
                    b1 += 1
            while(a1 < len(a)):
                res.append(a[a1])
                a1 += 1
            while(b1 < len(b)):
                res.append(b[b1])
                b1 += 1
            return res

        if(len(nums) == 1):
            return nums
        a = self.sortArray(nums[:len(nums)//2])
        b = self.sortArray(nums[len(nums)//2:])
        res = sortedMerge(a, b)
        return res
