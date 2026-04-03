class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for i,num in enumerate(nums):
            cop = target - num
            if cop in result:
                return [result[cop],i]
            result[num] = i