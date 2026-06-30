class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        key_val = {
            "]": "[",
            ")": "(",
            "}": "{"
        }
        
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) != 0 and key_val.get(s[i]) == stack[-1]:
                    stack.pop()
                else:
                    return False 
        
        return len(stack) == 0
