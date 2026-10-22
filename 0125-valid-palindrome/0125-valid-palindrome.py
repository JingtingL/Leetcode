class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = ""

        for c in s:
            if c.isalnum():
                cleaned += c.lower()
        
        # we don't care about the very middle if it is odd, bc either way it would be an palindrome
        for index in range(len(cleaned)//2): 
            if cleaned[index] != cleaned[-index - 1]:
                return False
        
        return True