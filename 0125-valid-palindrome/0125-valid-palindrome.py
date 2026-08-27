class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        
        for i in range(len(cleaned)//2):
            if cleaned[i] != cleaned[-i-1]:
                return False
        
        return True
        