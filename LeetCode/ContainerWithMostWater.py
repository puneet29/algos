class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_volume = 0
        max_height = max(height)
        left_idx = 0
        right_idx = len(height) - 1
        while left_idx < right_idx:
            left_wall = height[left_idx]
            right_wall = height[right_idx]
            width = (right_idx - left_idx)
            area = width * min(left_wall, right_wall)
            max_volume = max(max_volume, area)
            if max_height * width <= max_volume:
                break
            if left_wall > right_wall:
                right_idx -= 1
            else:
                left_idx += 1
        return max_volume
