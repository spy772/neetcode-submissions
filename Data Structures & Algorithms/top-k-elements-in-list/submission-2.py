class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums))]
        
        for num in nums:
            count[num] += 1
        for key, value in count.items():
            freq[value-1].append(key)

        ret_list = []
        for i in range(-1, -1 - len(freq), -1):
            for val in freq[i]:
                ret_list.append(val)
                if len(ret_list) == k:
                    return ret_list