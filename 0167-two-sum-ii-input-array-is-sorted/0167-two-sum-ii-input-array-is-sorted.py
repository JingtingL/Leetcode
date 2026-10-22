class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Since we are guaranteed length of numbers is at least 2
        # We can initialize two pointers
        left = 0
        right = len(numbers) - 1

        # Making sure we never go out of bound and left is always the left pointer
        while(left < right):
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left+1,right+1]
        
        return [-1,-1] # if nothing is found
        