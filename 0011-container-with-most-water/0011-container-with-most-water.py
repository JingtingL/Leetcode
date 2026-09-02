class Solution:
    def maxArea(self, height: List[int]) -> int:
        # In order to get area, we need 2 points
        left = 0
        right = len(height)-1
        result = 0

        while left<right:
            curr = min(height[left],height[right]) * (right - left)

            if curr > result:
                result = curr
            
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        
        return result



        


        