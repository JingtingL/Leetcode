class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        i = 0

        # 1) Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2) Read optional sign
        sign = 1
        if i < n and s[i] in '+-':
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3) Read digits and build number (with clamping)
        num = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # clamp before overflow
            if sign == 1:
                if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 7):
                    return INT_MAX
            else:
                if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 8):
                    return INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num
        # string_int = ""
        # sign = False
        # digit_start = False

        # for index in range(len(s)):

        #     if (string_int == "" and sign!= True):
        #         if s[index].isspace():
        #             continue
        #         elif s[index] == "-":
        #             sign = True
        #             string_int = "-"
        #         elif s[index] == "+":
        #             sign = True
        #             pass
        #         elif s[index].isdigit():
        #             digit_start = True
        #             string_int += s[index]
        #         else:
        #             break
        #     else:
        #         if not s[index].isdigit():
        #             break
        #         # once digits started, append ALL digits (including 0)
        #         string_int += s[index]

        # if string_int == "-" or string_int == "":
        #     return 0

        # num = int(string_int)
        # INT_MIN = -(2**31)
        # INT_MAX = (2**31) - 1

        # if num < INT_MIN:
        #     return INT_MIN
        # if num > INT_MAX:
        #     return INT_MAX
        # return num