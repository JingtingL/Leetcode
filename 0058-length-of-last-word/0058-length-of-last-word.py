class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                s = s[0:i+1]
                break
        
        for i in range(len(s)-1,-1,-1):
            if s[i] == " ":
                s = s[i+1:]
                break

        return len(s)