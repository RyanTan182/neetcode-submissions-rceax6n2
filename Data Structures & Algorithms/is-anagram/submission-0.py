class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        result = {}
        for char in s:
            if char in result:
                result[char] +=1
            else:
                result[char] = 1
        
        for chart in t:
            if result.get(chart,0) == 0:
                return False
            result[chart]-=1

        return True
        