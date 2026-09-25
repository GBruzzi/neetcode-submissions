class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for string in tokens:
            if string == "+":
                stack[-2] = stack[-2] + stack[-1]
                stack.pop()
    
            elif string == "*":
                stack[-2] = stack[-2] * stack[-1]
                stack.pop()

            elif string == "/":
                stack[-2] = int(stack[-2] / stack[-1])
                stack.pop()

            elif string == "-":
                stack[-2] = stack[-2] - stack[-1]
                stack.pop()

            else:
                stack.append(int(string))


        return stack[0]