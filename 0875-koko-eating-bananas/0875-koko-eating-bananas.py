class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # piles = [3,6,7,11], h = 8 
        # total = 27
        # Given this much bananas and I can only eat k amount per hour
        # I know I have a range from 1 to 11 of banana eating per hour:
        # I just need to calculate whether I can finish it under a certain number in that range using binary search

        # how do I know if I can finish it under that certain amount of hours
        # I feel like I can do if the certain amount * the number of piles is greater than or equal to the total banana in the file
        # 3 * 8 = 24
        # 4 * 8 = 32

        # piles = [30,11,23,4,20], h = 5
        # 30 + 11 + 23 + 4 + 20 = 88
        # 30 * 5 = 150
        # 23 * 5 = 115 , so no this would not work --> so our lower limit must be biggest number // (len(pile) // h)

        # This function will give us with the k speed, how much hour we need to eat everything
        def hours_needed(k):
            total = 0
            for pile in piles:
                total += (pile + k - 1) // k   # hours for this one pile, rounded up
            return total

        left = 1
        right = max(piles)
        answer = right # sometimes no speed can hit h exactly

        while left <= right:
            # mid represents the bananas we are eating per hour
            mid = (right + left) // 2

            if hours_needed(mid) <= h: # if we can complete everything early, that means we can eat less banana
                right = mid - 1
                answer = mid # save the answer, but try eating less and see if it will still work
            else: # if we cannot complete everything, that means we need to eat more banana 
                left = mid + 1
        
        return answer



        