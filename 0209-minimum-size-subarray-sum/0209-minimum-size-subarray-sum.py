class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        shortest = float('inf')
        left = 0
        running_total = 0

        for right in range(0,len(nums)):
            # adding the current
            running_total += nums[right]
            
            while running_total >= target:
                shortest = min(right - left +1, shortest)
                running_total -= nums[left]
                left +=1

        return 0 if shortest == float('inf') else shortest  


