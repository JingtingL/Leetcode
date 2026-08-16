class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        num = str(x) # making sure we can iterate through each characters

        if ("-" in num): # if number is negative, we know it is not a palindrome
            return False
        
        total_ind = len(num) -1 

        # We can always skip checking the middle number if odd bc it is shared
        for i in range(len(num)//2): # 5//2 = 2 4//2=2 
            if (num[i] != num[total_ind - i]): # checks (ind 0, ind 2)
                return False
        
        return True
        


        