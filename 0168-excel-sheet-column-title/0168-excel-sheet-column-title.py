class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # A = 1
        # AA = 1 + 26
        # So I need to find the % 26
        # each time I need to update the number by //26
        # I need to do this until the the columnNumber is equal or less than 0
        letters = ""
        title = {0:"Z", 1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I"
        , 10:"J", 11:"K", 12:"L", 13:"M", 14:"N", 15:"O", 16:"P", 17:"Q", 18:"R"
        , 19:"S", 20:"T", 21:"U", 22:"V", 23:"W", 24:"X", 25:"Y"}
        while columnNumber > 0:
            letterNumber = columnNumber % 26
            letters = title[letterNumber] + letters
            if columnNumber % 26 == 0:
                columnNumber = columnNumber//26 -1
            else:
                columnNumber = columnNumber//26

        return letters

        # 701
        # 701 % 26
        