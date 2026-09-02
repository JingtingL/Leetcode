class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def recurse(current, open, close):
            if open == n and close == n:
                result.append(current)
                return
            
            if open < n:
                recurse(current+"(",open+1,close)
            if close < open:
                recurse(current+")",open, close+1)
        
        recurse("",0,0)
        return result
