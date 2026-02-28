class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        # base case
        if (numRows == 1):
            return s
        
        res = ""
        # we want to go down row by row
        for row in range (numRows):
            increment = (numRows - 1) * 2

            for index in range(row, len(s) ,increment):
                res += s[index]

                if(row != 0    and     row != numRows-1     and     index + increment - row*2 < len(s)):
                    res += s[index + increment - row*2]
        
        return res