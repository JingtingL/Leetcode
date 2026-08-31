class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #abcabcbb
        #a --> ab --> abc --> abca
        # I want to start from the beginning to remove the duplicate if it is the same, and I need a way to know whether there is still duplicate
        # set length comparison tells me whether there are still duplicates
        # to start from the beginning of the substring I need a way to track the index of the beginning
        # everytime before I update I need to update the max first

        # Solution 1
        # result = 0
        # substring = ""

        # for i in range(len(s)):
        #     # remove duplicates
        #     if s[i] in substring:
        #         #print("currently there is " + s[i] + " in " + substring)
        #         result = max(result,len(substring))
        #         while s[i] in substring: 
        #             #print("removing " + substring[0])
        #             substring = substring[1:]
        #         #print("now there is only " + substring)
            
        #     substring += s[i]
        #     #print("added " + s[i] + " to make " + substring)
        
        # result = max(result,len(substring))
        # return result

        seen = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            result = max(result, right - left + 1)
        
        return result


        