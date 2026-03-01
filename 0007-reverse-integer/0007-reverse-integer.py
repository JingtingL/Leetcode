class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string_x = str(x)
        sign = ""
        string_rst = ""

        for index in range(len(string_x)):
            if(index == 0 and string_x[0] == "-"):
                sign = string_x[0]
                continue
            
            # always append to the front
            string_rst = string_x[index] + string_rst

        if (sign == "-"):
            string_rst = sign + string_rst

        # computing the result
        if (-2**31 <= int(string_rst) <= 2**31 - 1):
            rst = int(string_rst)
        else:
            rst = 0

        return rst

            


        