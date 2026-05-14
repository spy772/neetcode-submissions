class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_speed = r

        while l <= r:
            mid = (l + r) // 2
            
            total_time = 0
            for banana in piles:
                total_time += math.ceil(banana / mid)

            if total_time <= h:
                min_speed = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return min_speed
