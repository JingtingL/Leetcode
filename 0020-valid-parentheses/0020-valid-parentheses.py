class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {"(":")", "{":"}", "[":"]"}
        stack = []

        for element in s:
            if element in brackets:
                stack.append(element)
            else:
                if len(stack) == 0:
                    return False
                elif brackets[stack.pop()] != element:
                    return False

        if len(stack) != 0:
            return False
        return True 