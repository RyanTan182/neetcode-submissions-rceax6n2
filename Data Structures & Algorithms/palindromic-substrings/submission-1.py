class Solution:
    def checkPalindorme(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    def countSubstrings(self, s: str) -> int:
        res = len(s)
        for i in range(1, len(s)):
            for j in range(i):
                if self.checkPalindorme(s[j:i + 1]):
                    res += 1
        return res

        