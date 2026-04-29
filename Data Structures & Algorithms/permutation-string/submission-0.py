class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s2_len < s1_len:
            return False

        char_count = defaultdict(int)
        s1_count = defaultdict(int)
        for char in s1:
            s1_count[char] += 1

        l = 0
        for r in range(s2_len):
            char_count[s2[r]] += 1
            if r - l + 1 == s1_len:
                if char_count == s1_count: 
                    return True

                char_count[s2[l]] -= 1

                if char_count[s2[l]] == 0:
                    del char_count[s2[l]] 

                l += 1
            
            r += 1
            
        return False