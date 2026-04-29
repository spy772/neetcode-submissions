class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            diff = r - l
            min_height = min(heights[l], heights[r])
            if min_height * diff > area:
                area = min_height * diff
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return area