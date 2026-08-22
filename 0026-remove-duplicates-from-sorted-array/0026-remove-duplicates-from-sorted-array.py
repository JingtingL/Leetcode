class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        smallest = -101
        for i in range(len(nums)):
            if nums[i] != smallest:
                smallest = nums[i]
                nums[k] = smallest
                k+=1
        return k
        

        