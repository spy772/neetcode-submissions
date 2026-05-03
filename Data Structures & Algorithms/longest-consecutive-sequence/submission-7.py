class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        if len(num_set) == 0 or len(num_set) == 1:
            return len(num_set)

        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(length, longest)

        return longest
                