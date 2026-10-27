class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        # this will calculate whether the k capacity of a ship will work in d days
        def neededDay(k):
            total = 0
            ship = 1 # always start with 1 ship already
            for weight in weights:
                # first check if the weight can still be loaded on this ship
                if total + weight > k:
                    ship += 1
                    total = 0
                total += weight

            return ship
        
        left = max(weights)
        right = sum(weights)
        answer = right

        while left <= right:
            # mid represents the total capacity of one ship, which is the load for one day
            mid = (right + left) // 2

            if neededDay(mid) <= days: # if we needed less ships than required, save the answer try less capacity
                right = mid - 1
                answer = mid
            else: # otherwise we need to increase the weight capacity so we can make it in d days
                left = mid + 1
        return answer


        