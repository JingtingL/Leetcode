class Solution:
    def convert(self, s: str, numRows: int) -> str:
        buckets = [""] * numRows
        row = 0
        direction = 1 # Rule: 1 is up, -1 is down

        if numRows == 1:
            return s

        for i in range(len(s)):

            # determine the direction of the zigzag
            if row == 0:
                direction = 1
            elif row == numRows-1:
                direction = -1
            
            # add to the back of the string
            buckets[row] += s[i]
            # iterate through the rows
            row += direction
        
        result = ""
        for row in range(numRows):
            result += buckets[row]
        return result
            


