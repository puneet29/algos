class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        global_max_volume = -1
        left_idx = 0
        while left_idx < len(height):
            left_wall = height[left_idx]
            max_volume = global_max_volume
            right_idx = len(height) - 1
            while right_idx > left_idx:
                w = right_idx - left_idx
                if left_wall * w <= max_volume:
                    break
                right_wall = height[right_idx]
                h = min(right_wall, left_wall)
                max_volume = max(max_volume, w * h)
                right_idx -= 1
            global_max_volume = max(global_max_volume, max_volume)
            left_idx += 1
        return global_max_volume
