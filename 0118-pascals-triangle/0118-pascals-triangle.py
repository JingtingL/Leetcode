class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Start with the base case
        result = [[1]]

        for _ in range(numRows-1):
            prev = result[-1] # Always look at the last row
            newRow = [1] # pascal always start with 1

            for i in range(1,len(prev)):
                newRow.append(prev[i] + prev[i-1])
            
            newRow.append(1)
            result.append(newRow)

        return result
        