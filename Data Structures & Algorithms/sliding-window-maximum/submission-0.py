class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        ret_list = []

        while r < len(nums):
            curr_set = nums[l:r+1].copy()
            curr_set.sort()
            ret_list.append(curr_set[-1])
            l += 1
            r += 1
        
        return ret_list