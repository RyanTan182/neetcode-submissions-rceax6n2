class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        left = 0
        right = k - 1

        while right < len(nums):
            maxNum = nums[left]
            for i in range(left, right + 1):
                if nums[i] > maxNum:
                    maxNum = nums[i]
            result.append(maxNum)
            left += 1
            right += 1
        
        return result

        