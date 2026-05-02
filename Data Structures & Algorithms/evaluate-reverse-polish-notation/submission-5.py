class Solution:
    def is_numeric_value(self, val):
        try:
            float(val)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.is_numeric_value(token):
                stack.append(int(token))
            else:
                if len(stack) > 1:
                    val_1 = stack.pop()
                    val_2 = stack.pop()
                    if token == "+":
                        new_val = val_2 + val_1
                    elif token == "-":
                        new_val = val_2 - val_1 # Order matters
                    elif token == "*":
                        new_val = val_2 * val_1
                    elif token == "/":
                        new_val = int(val_2 / val_1) # Order matters
                    
                    stack.append(new_val)
        
        return stack[-1]