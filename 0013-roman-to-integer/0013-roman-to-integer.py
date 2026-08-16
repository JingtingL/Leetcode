class Solution:
    def romanToInt(self, s: str) -> int:
        # Take for example "MCMXCIV"
        num = 0
        kv = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        last = len(s) - 1

        for i in range(last):
            curr_letter = s[i]
            next_letter = s[i+1]
            
            # look at the next number
            if kv[curr_letter] < kv[next_letter]:
                num += kv[curr_letter] * -1
            else:
                num += kv[curr_letter]

        num += kv[s[last]]        
        return num