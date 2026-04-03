class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashSet = []
        for i in range(len(nums)):
            hashSet.append(nums[i])
        print(hashSet)
        
        for j in range(len(nums) + 1):
            print()
            if j not in hashSet:
                return j

        return 0 
        