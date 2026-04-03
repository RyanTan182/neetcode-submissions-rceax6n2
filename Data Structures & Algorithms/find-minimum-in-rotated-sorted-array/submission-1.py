class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_no = nums[0]

        for i in range(len(nums)):
            if min_no > nums[i]:
                min_no = nums[i]

        return min_no
        