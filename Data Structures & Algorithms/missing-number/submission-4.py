class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashSet = []
        for i in range(len(nums)):
            hashSet.append(nums[i])
        
        for j in range(len(nums) + 1):
            if j not in hashSet:
                return j

        return 0 
        