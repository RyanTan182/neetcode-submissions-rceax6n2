class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count+=1
            else:
                product *= num

        result = []
        for i,v in enumerate(nums):
            if zero_count > 1:
                result.append(0)
            elif zero_count == 1:
                if v == 0:
                    result.append(product)
                else:
                    result.append(0)
            else:
                result.append(product // v)
        return result

        