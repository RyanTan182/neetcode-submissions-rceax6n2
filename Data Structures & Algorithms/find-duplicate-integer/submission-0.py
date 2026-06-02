class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dictionary = {}
        for i in range(len(nums)):
            if dictionary.get(nums[i], 0) > 0:
                return nums[i]
            else:
                dictionary[nums[i]] = 1 + dictionary.get(nums[i], 0)
        
        

        