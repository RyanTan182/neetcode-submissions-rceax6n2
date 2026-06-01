class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(0, len(tokens)):
            if tokens[i] == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif tokens[i] == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif tokens[i] == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif tokens[i] == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(tokens[i]))

        return stack[0]