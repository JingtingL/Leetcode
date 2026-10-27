class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # nums = [4,5,6,7,0,1,2], target = 0
        # if the array is left rotated then there will be a pivot point
        left = 0
        right = len(nums) - 1

        while left <= right:
            # check if the left half is sorted
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # check if the left half is sorted
            if nums[left] <= nums[mid]:
                # I want to check whether the target value is in the range
                if nums[left] <= target < nums[mid]:
                    # search the left side
                    right = mid - 1
                else:
                    left = mid + 1 
            # otherwise the right side is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1



