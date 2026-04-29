class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret_hash = {}
        for string in strs:
            char_counts = [0] * 26
            for ch in string:
                char_counts[ord(ch) - ord('a')] += 1

            if str(char_counts) in ret_hash:
                ret_hash[str(char_counts)].append(string)
            else:
                ret_hash[str(char_counts)] = [string]

        return list(ret_hash.values())