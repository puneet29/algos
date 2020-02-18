class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def binsearch(arr, target, low, high):
            """
            :type arr: List[int]
            :type target: int
            :rtype: bool
            """
            if(low > high):
                return False
            mid = (low+high)//2
            if(arr[mid] == target):
                return True
            if(arr[mid] > target):
                high = mid - 1
            else:
                low = mid + 1
            return binsearch(arr, target, low, high)

        for arr in matrix:
            if(binsearch(arr, target, 0, len(arr)-1)):
                return True
        return False
