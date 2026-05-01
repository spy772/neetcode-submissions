class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: # By definition cannot have odd lengths
            return False

        brackets = {'{': '}', '(': ')', '[': ']'}
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                
                start_char = stack.pop()
                correct = False
                for key, value in brackets.items():
                    if start_char == key and char == value:
                        correct = True
                        break
                
                if not correct:
                    return False
            
        return len(stack) == 0

