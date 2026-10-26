class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # using a hashmap to remember which letter is the most frequent
        counts = {}
        left = 0
        best = 0
        for right in range(0, len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            changes = (right - left + 1) - max(counts.values())
            while changes > k:
                counts[s[left]] -= 1
                left += 1
                changes = right - left - max(counts.values())
            best = max(best, right - left + 1)
        return best