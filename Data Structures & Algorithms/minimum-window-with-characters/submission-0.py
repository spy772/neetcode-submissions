class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ret_str = ""
        len_s, len_t = len(s), len(t)
        if len_t > len_s: # Cannot have t > s by definition
            return ret_str

        t_count = defaultdict(int)
        for char in t:
            t_count[char] += 1
        
        curr_count = defaultdict(int)
        have, need = 0, len(t_count)  # need = distinct chars in t
        l = 0
        result = ""

        for r in range(len(s)):
            curr_count[s[r]] += 1
            # Check if this char just satisfied its required count
            if s[r] in t_count and curr_count[s[r]] == t_count[s[r]]:
                have += 1

            while have == need:  # Valid window, shrink if possible
                new_str = s[l:r+1]
                if ret_str == "" or len(new_str) < len(ret_str):
                    ret_str = new_str

                curr_count[s[l]] -= 1
                if s[l] in t_count and curr_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1

        return ret_str
