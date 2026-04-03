class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for i, num in enumerate(nums):
            if num in result:
                return True
            result[num] = num
        return False            
        