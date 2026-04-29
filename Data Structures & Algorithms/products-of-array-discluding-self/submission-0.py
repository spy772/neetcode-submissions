class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        num_zeroes = 0
        for num in nums:
            if num == 0:
                num_zeroes += 1
                if num_zeroes == 2:
                    return [0] * len(nums)
            else:
                total_prod *= num
        
        ret_list = []
        for num in nums:
            if num == 0:
                ret_list.append(total_prod)
            elif num_zeroes == 1:
                ret_list.append(0)
            else:
                ret_list.append(int(total_prod / num))

        return ret_list
