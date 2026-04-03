class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        final_result = []

        for left in range(n-2):
            if nums[left] > 0:
                break
            if left > 0 and nums[left] == nums[left-1]:
                continue
            mid = left + 1
            right = n - 1

            while mid < right:
                print("Nums left:", nums[left])
                print("Nums mid:", nums[mid])
                print("Nums right:", nums[right])

                sum = nums[left] + nums[mid] + nums[right]

                if sum == 0:
                    final_result.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1
                    mid += 1
                    right -= 1
                elif sum < 0:
                    mid += 1
                elif sum > 0:
                    right -= 1

        return final_result
        