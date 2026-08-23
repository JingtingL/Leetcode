class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seens = set()
        for element in nums:
            if element not in seens:
                seens.add(element)
            else:
                return True
        
        return False