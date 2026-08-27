class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # base case
        prev = [1]

        if rowIndex == 0:
            return prev
        
        for _ in range(rowIndex):
            newRow = [1]

            for i in range(1,len(prev)):
                newRow.append(prev[i] + prev[i-1])
            
            newRow.append(1)
            prev = newRow
        
        return prev
        