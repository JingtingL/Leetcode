class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # [73,74,75,71,69,72,76,73]
        # I want to be able to go through each element achieving O(n)
        # I want to keep track of the cooler days and their index
        # I know that cooler days will be on top, so I just need to compare the top day with the current
        stack = []
        result = [0] * len(temperatures)
        for i in range(0,len(temperatures)):
            temp = temperatures[i]
            # base case
            if len(stack) == 0:
                stack.append((temp, i))
                continue
            
            # while our current temperature is greater than the prior temperature
            while len(stack) > 0 and temp > stack[-1][0]:
                count = i - stack[-1][1]
                result[stack[-1][1]] = count
                stack.pop()
            
            stack.append((temp, i))
        
        return result


        