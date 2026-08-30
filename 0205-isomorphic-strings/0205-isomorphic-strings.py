class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # egg --> add
        # e --> a: this mapping makes me think of dictionary
        # g --> d
        # first of all i know I need to go thorugh every letter
        # I think I need to check 
        lut = {}
        seen = set()


        for i in range(len(s)):
            if t[i] in lut and lut[t[i]] != s[i]:
                return False
            elif t[i] in lut and lut[t[i]] == s[i]:
                continue
            elif t[i] not in lut and s[i] not in seen:
                lut[t[i]] = s[i]
                seen.add(s[i])
            else:
                return False
        
        return True