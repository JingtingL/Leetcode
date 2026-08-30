class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}

        for element in nums:
            if element in elements:
                elements[element] +=1
            else:
                elements[element] = 1
        
        print(str(elements))
        max = 0
        value = ""
        for element in elements:
            if elements[element] > max:
                max = elements[element]
                value = element
                print("max: " + str(max))
                print("value: " + str(value))
        
        return value
            
        
            
        