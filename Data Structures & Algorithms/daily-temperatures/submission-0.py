class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        stack = []

        for i in range(n):
            for j in range(i + 1, n):
                stack.append(temperatures[j])
                if temperatures[j] > temperatures[i]:
                    res[i] = len(stack)
                    break
            stack.clear()
        return res

        
        