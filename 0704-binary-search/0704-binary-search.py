class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # since the list is sorted from small to biggest
        # we can look at the middle number each time compare 
        # whether that is smaller or bigger than our middle
        # if it is equal we return that 

        # nums = [-1,0,3,5,9,12]
        # index = [0,1,2,3,4,5]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left // 2) # integer division
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

