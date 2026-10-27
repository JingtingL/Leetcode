class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        if len(s) <  len(t):
            return result

        # first I want to count what I actually need
        need = {}
        for i in range(0, len(t)):
            need[t[i]] = need.get(t[i], 0) + 1

        # now I want to build a window of what is valid first
        window = {}
        left = 0
        best_len = float('inf')
        best_start = 0
        
        for right in range(0, len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            # check whether the window is valid
            valid = True
            for c in need:
                if window.get(c,0) < need[c]:
                    valid = False
                    break

            # while the window is valid
            while valid:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                # then I want to remove s[left] from the window
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left+= 1

                for c in need:
                    if window.get(c,0) < need[c]:
                        valid = False
                        break

        return "" if best_len == float('inf') else s[best_start : best_start + best_len]