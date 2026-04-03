class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            print("Height on left:",heights[left])
            print("Height on right:",heights[right])
            sumArea = min(heights[left],heights[right]) * (right - left)
            print("SumArea:", sumArea)
            if sumArea > max_area:
                print("Yess!")
                max_area = sumArea
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
        
        