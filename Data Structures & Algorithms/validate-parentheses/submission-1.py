class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == ']' and len(stack) > 0:
                j = stack.pop()
                if j != '[':
                    return False
            elif i == '}' and len(stack) > 0:
                j = stack.pop()
                if j != '{':
                    return False
            elif i == ')' and len(stack) > 0:
                j = stack.pop()
                if j != '(':
                    return False
            else:
                stack.append(i)
        
        if len(stack) > 0:
            return False
        return True
        