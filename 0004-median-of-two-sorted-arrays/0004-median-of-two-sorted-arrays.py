class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        m, n = len(A), len(B)

        # Ensure A is the smaller array
        if m > n:
            A, B = B, A
            m, n = n, m

        total = m + n
        half = (total + 1) // 2  # left side size

        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2      # cut in A
            j = half - i            # cut in B

            Aleft  = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i]     if i < m else float("inf")
            Bleft  = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j]     if j < n else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                # Correct partition
                if total % 2 != 0:
                    return float(max(Aleft, Bleft))
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0

            elif Aleft > Bright:
                hi = i - 1
            else:
                lo = i + 1

        # Should never happen if inputs are valid sorted arrays
        return 0.0
        
        
        # m, n = len(nums1), len(nums2)
        # lst = []
        # i = j = 0

        # while (i < m and j < n):
        #     if (nums1[i] <= nums2[j]):
        #         lst.append(nums1[i])
        #         i+=1
        #     elif (nums2[j] < nums1[i]):
        #         lst.append(nums2[j])
        #         j+=1

        # # draining the rest
        # while (i < m):
        #     lst.append(nums1[i])
        #     i+=1
        # while (j < n):
        #     lst.append(nums2[j])
        #     j+=1
        
        # # if odd, then grab the middle number
        # total = m + n
        # med = total // 2

        # if (total%2 != 0):
        #     median = float(lst[med])
        #     return median
        # # if even, then grab the 2 middle point and average it out
        # else:
        #     median = (lst[med] + lst[med -1]) / 2.0
        #     return median




        