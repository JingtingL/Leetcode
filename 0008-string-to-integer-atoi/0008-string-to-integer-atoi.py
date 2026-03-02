class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        string_int = ""
        sign = False
        digit_start = False

        for index in range(len(s)):

            if (string_int == "" and sign!= True):
                if s[index].isspace():
                    continue
                elif s[index] == "-":
                    sign = True
                    string_int = "-"
                elif s[index] == "+":
                    sign = True
                    pass
                elif s[index].isdigit():
                    digit_start = True
                    string_int += s[index]
                else:
                    break
            else:
                if not s[index].isdigit():
                    break
                # once digits started, append ALL digits (including 0)
                string_int += s[index]

        if string_int == "-" or string_int == "":
            return 0

        num = int(string_int)
        INT_MIN = -(2**31)
        INT_MAX = (2**31) - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num