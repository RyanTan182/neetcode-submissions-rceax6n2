class Solution:
    # def checkPalindrome(self, s:str, l:int, r:int) -> bool:
    #     while l < r:
    #         if s[l] != s[r]:
    #             return False
    #         l += 1
    #         r -= 1
    #     return True
    def longestPalindrome(self, s: str) -> str:
        #1st Approach: 2Pointers - O(n^3)
        # res, maxLen = "",0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         l,r=i,j
        #         while l < r and s[l] == s[r]:
        #             l += 1
        #             r -= 1
                
        #         if l >= r and maxLen < (j - i + 1):
        #             res = s[i: j + 1]
        #             maxLen = j - i + 1
        # return res

        #2nd Approach: DP - O(n^2)
        # resIdx, maxLen = 0,0
        # n = len(s)
        # dp = [[False] * n for _ in range(n)]
        # for i in range(n - 1, -1, -1):
        #     for j in range(i, n):
        #         if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
        #             dp[i][j] = True
        #             if maxLen < (j - i + 1):
        #                 resIdx = i
        #                 maxLen = j - i + 1
        # return s[resIdx: resIdx + maxLen]

        # 3rd Approach: 2Pointers (Expand from Center) - O(n^2)
        resIdx, maxLen = 0,0
        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if maxLen < (r- l + 1):
                    maxLen = r - l + 1
                    resIdx = l
                l -= 1
                r += 1
            
            l,r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if maxLen < (r - l + 1):
                    maxLen = r - l + 1
                    resIdx = l
                l -= 1
                r += 1
            
        return s[resIdx: resIdx + maxLen]


        