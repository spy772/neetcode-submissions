class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        l, r = 0, 0
        longest = 0
        char_set = set()
        while r < len(s):
            if s[r] in char_set:
                longest = max(r - l, longest)
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l += 1

            char_set.add(s[r])
            r += 1

        return max(longest, len(s) - l)
            


