class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        if n <= 1:
            return s

        best_l, best_r = 0, 0  # inclusive indices

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            # went one step too far, so return the last valid window
            return l + 1, r - 1

        for i in range(n):
            # odd length
            l1, r1 = expand(i, i)
            if r1 - l1 > best_r - best_l:
                best_l, best_r = l1, r1

            # even length
            l2, r2 = expand(i, i + 1)
            if r2 - l2 > best_r - best_l:
                best_l, best_r = l2, r2

        return s[best_l:best_r + 1]