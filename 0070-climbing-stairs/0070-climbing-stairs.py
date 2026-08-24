class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 
        #1 way
        
        # 1 + 1
        # 2
        # 2 ways

        # 1 + 1 + 1
        # 2 + 1
        # 1 + 2
        # 3 ways

        # 1 + 1 + 1 + 1
        # 2 + 1 + 1
        # 1 + 2 + 1
        # 1 + 1 + 2
        # 2 + 2
        # 5 ways

        # 1 + 1 + 1 + 1 + 1
        # 2 + 1 + 1 + 1
        # 1 + 2 + 1 + 1
        # 

        # Maybe something like first figure out how many 1 is needed to become the number, say 45
        # Then, figure out how many times those 1s can become a 2
        # Wait actually I think this is F(n) = F(n-1) + F(n-2)

        # This words (Way 1 Recursion)
        # if n == 1: return 1 # base case 1
        # if n == 2: return 2 # base case 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        if n == 1: 
            return 1 
        else: prev1 = 1
        
        if n == 2: 
            return 2 
        else: prev2 = 2

        for i in range(3, n+1):
            result = prev1 + prev2
            prev1 = prev2
            prev2 = result
        return result



        