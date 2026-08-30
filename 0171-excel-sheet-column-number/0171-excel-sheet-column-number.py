class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for i in range(len(columnTitle)-1,-1, -1):
            print(i)
            iteration = len(columnTitle)-1 - i
            letter = columnTitle[i]
            number = ord(letter) - 64 # This make sure A is 1 instead of 0

            if iteration == 0:
                total += number
                print("iteration: " + str(iteration) + " number: " + str(number))
                print("total: " + str(total))
            else:
                 num = (26 ** iteration) * (number)
                 total += num
                 print("iteration: " + str(iteration) + " number: " + str(number) + " num: " + str(num))
                 print("total: " + str(total))

        return total

        #AB
        # B = 2
        # to reach level A, it is 26 * 1
        # 26^1 * 1 --> iteration, number



        #ZY
        # Y = 25
        # To reach the Z level in the second tier, it is 26*26
        # 26^1 * 26



        # when num <= 26, we can directly add the letterSequence
        # when num > 26, we want to subtract 





        