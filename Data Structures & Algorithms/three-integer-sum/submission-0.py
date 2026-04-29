class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        ret_list = []

        for curr in range(len(sorted_nums)):
            l, r = curr + 1, len(sorted_nums) - 1
            while l < r:
                lr_sum = sorted_nums[l] + sorted_nums[r]
                if sorted_nums[curr] + lr_sum == 0:
                    new_triplet = [sorted_nums[curr], sorted_nums[l], sorted_nums[r]]
                    if new_triplet not in ret_list: ret_list.append(new_triplet)
                    r -= 1
                elif sorted_nums[curr] + lr_sum > 0:
                    r -= 1
                else:
                    l += 1
        
        return ret_list