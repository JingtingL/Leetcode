class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #numbers = {}

        #for element in nums:
        #    if element in numbers:
        #        numbers[element] +=1
        #    else:
        #        numbers[element] = 1
            
        # find the element with value 1
        #for key, value in numbers.items():
        #    if value == 1:
        #        return key

        result = 0
        for num in nums:
            result = result ^ num
        return result