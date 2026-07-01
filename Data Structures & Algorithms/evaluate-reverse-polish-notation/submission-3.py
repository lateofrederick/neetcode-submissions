class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif i == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2 / val1))
            else:
                stack.append(int(i))
        
        return stack[0] if stack else 0
