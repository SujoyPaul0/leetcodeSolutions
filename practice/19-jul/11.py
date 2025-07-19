class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(height) - 1
        left, right = height[l], height[r]

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxArea = max(area, maxArea)
            if height[l] < height[r]:
                l += 1
                if height[l] > left or l == 0:
                    area = min(height[l], height[r]) * (r - l)
                    maxArea = max(area, maxArea)
                    left = max(height[l], left)
            else:
                r -= 1
                if height[r] > right:
                    area = min(height[l], height[r]) * (r - l)
                    maxArea = max(area, maxArea)
                    left = max(height[r], right)

        return maxArea
