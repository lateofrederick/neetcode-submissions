class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            # if is type number add to stack
            # else if is an operator
            # pop the last two items and perform operation
            if i in ["+", "*", "-", "/"] and stack:
                val1 = stack.pop()
                val2 = stack.pop()
                if i == "+":
                    stack.append(val1 + val2)
                if i == "*":
                    stack.append(val1 * val2)
                if i == "-":
                    stack.append(val2 - val1)
                if i == "/":
                    stack.append(int(val2 / val1))
            else:
                stack.append(int(i))
        
        return stack[0] if stack else 0
