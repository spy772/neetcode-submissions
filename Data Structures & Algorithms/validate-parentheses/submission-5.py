class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: # By definition cannot have odd lengths
            return False

        end_chars = {'}': '{', ')': '(', ']': '['}
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                
                if stack[-1] == end_chars[char]:
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0

