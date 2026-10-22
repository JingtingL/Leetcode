class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        seen = {0:1} # we start at location 0 SO 0%5 = 0
        running_total = 0
        count = 0

        for index in range(len(nums)):
            running_total += nums[index] # keeps track of the sum

            # I want to find the remainder of this number divided by k
            target = running_total % k

            # I just need to remember how many times I had encounter this remainder
            # This is because the same remainder subtracted by the same remainder
            # cancels out
            if target in seen:
                count += seen[target]
            
            # We are trying to save the remainder, so we can add it the next time we see it
            seen[target] = seen.get(target,0) + 1
        
        return count

            