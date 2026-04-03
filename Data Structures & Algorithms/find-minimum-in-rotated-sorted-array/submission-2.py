class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_no = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right) // 2
            min_no = min(min_no, nums[mid])

            if nums[mid] > nums[right]:
                min_no = min(min_no, nums[left])
                left = mid + 1
            else:
                min_no = min(min_no, nums[mid])
                right = mid - 1

        return min_no