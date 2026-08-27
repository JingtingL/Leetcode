class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # base case
        result = [[1]]

        if rowIndex == 0:
            return result[-1]
        
        for _ in range(rowIndex):
            prev = result[-1]
            newRow = [1]

            for i in range(1,len(prev)):
                newRow.append(prev[i] + prev[i-1])
            
            newRow.append(1)
            result.append(newRow)
        
        return result[-1]
        