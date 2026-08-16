class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        stringA = strs[0] # assume this is the current prefix
        for word_index in range(1,len(strs)):
            stringB = strs[word_index]
            temp = ""
            word_length = min(len(stringA), len(stringB))
            for i in range(word_length):
                if (stringA[i] == stringB[i]):
                    temp += stringA[i]
                else:
                    stringA = temp
                    break
            stringA = temp
        
        return stringA




        