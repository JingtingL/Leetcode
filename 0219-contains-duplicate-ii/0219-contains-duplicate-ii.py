class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lut = {}

        for i in range(len(nums)):
            if nums[i] in lut:
                 calculation = i - lut[nums[i]]
                 print(str(i) + " " + str(lut[nums[i]]))
                 if calculation <= k: return True
            #      else: lut[nums[i]] = i
            # else:
            lut[nums[i]] = i
        
        return False
        