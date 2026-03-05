class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # searching for something uses binary search
        # binary search is O(log n) runtime

        mid = 0
        left = 0
        right = len(nums) - 1
        
        while (left <= right):
            # calculate the middle index using integer division
            mid = (left + right)//2

            # if the target is the mid element, return that
            if nums[mid] == target:
                return mid

            # if target is greater than the mid element ignore the left half
            elif nums[mid] < target:
                left = mid + 1
            
            # if target is less than the mid element ignore the right hald
            else:
                right = mid - 1

        # if the target finishes without finding the target, then return the middle point of 
        return left
        