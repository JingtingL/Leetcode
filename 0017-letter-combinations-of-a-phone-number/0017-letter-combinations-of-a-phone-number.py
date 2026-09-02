class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        numbers = {"2":['a','b','c'], "3":['d','e','f'], "4":['g','h','i'], "5":['j','k','l'], "6":['m','n','o'], "7":['p','q','r','s'], "8":['t','u','v'], "9":['w','x','y','z']}

        def recurse(index,current):
            # base case to use all digits
            if index == len(digits):
                result.append(current)
                return
            
            for letter in numbers[digits[index]]:
                recurse(index+1,current+letter)
            
        recurse(0,"")
        return result

            
        