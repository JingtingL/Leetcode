class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []

        # make sure s has enough character to cover all of p's length
        if len(s) < len(p):
            return result
        
        # building a memory for comparison
        k = len(p)
        counts = {}
        for i in range(0, k):
            counts[p[i]] = counts.get(p[i], 0) + 1
        
        # build a window
        window = {}
        for i in range(0, k):
            window[s[i]] = window.get(s[i], 0) + 1
        if window == counts:
            result.append(0)

        # scanning through the rest of the window to find the index with the anagram
        for i in range(k, len(s)):
            new = s[i]
            window[new] = window.get(new, 0) + 1

            # remove the old 
            old = s[i - k]
            window[old] -= 1
            if window[old] == 0:
                del window[old]
            
            # checking if the window is a anagram
            if window == counts:
                result.append(i - k + 1)
            

        return result