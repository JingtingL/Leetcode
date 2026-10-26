class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 = "ab"
        # s2 = "eidbaooo"
        if len(s1) > len(s2):
            return False
        
        counts = {} # at most store 26 letters
        k = len(s1)

        # remember what s1 needs
        for i in range(len(s1)):
            counts[s1[i]] = counts.get(s1[i],0) + 1
        
        
        seen = {}
        # build the first window
        for i in range(0,k):
            seen[s2[i]] = seen.get(s2[i], 0) + 1
        # check whether the window is equal to the count
        if seen == counts:
            return True


        # otherwise, we keep sliding the window one by one and checking it
        for i in range(k, len(s2)):
            seen[s2[i]] = seen.get(s2[i], 0) + 1

            # remove the old letter
            old = s2[i - k]
            seen[old] -= 1
            if seen[old] == 0:
                del seen[old]
            
            # check whether the two hashmaps are equal
            if seen == counts:
                return True

        return False    
                    




            
        

        

        
        