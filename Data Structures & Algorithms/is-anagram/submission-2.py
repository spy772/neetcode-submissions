class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_char = {}

        for ch in s:
            if ch in hash_char:
                hash_char[ch] += 1 
            else:
                hash_char[ch] = 1
        
        for ch in t:
            if ch not in hash_char or hash_char[ch] == 0:
                return False
            
            hash_char[ch] -= 1

        return True