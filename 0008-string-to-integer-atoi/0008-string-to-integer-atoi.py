class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        left = 0
        result = 0

        # base case
        if len(s) == 0:
            return 0

        # step 1 
        for i in range(len(s)):
            if s[i] == " ":
                continue
            else:
                left = i
                break
        
        # step 2
        if s[left] == "-":
            left += 1
            sign = -1
        elif s[left] == "+":
            left += 1
            sign = 1
        
        # step 3
        for i in range(left,len(s),1):
            if s[i].isdigit():
                result = result * 10 + (ord(s[i]) - ord('0'))
            else:
                break
        
        # step 4
        result = result * sign

        if result < 0:
            result = max(result, -2**31)
        else:
            result = min(result, 2**31 - 1)
        
        return result
        

            



