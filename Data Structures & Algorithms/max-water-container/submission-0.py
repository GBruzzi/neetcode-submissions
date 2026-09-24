class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)

        res = 0

        l = 0
        r = n - 1

        while l < r:
            water = (r - l) * min(height[l],height[r])

            if water > res:
                res = water

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res
