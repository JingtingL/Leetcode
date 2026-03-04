class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        lst = []
        i = j = 0

        while (i < m and j < n):
            if (nums1[i] <= nums2[j]):
                lst.append(nums1[i])
                i+=1
            elif (nums2[j] < nums1[i]):
                lst.append(nums2[j])
                j+=1

        # draining the rest
        while (i < m):
            lst.append(nums1[i])
            i+=1
        while (j < n):
            lst.append(nums2[j])
            j+=1
        
        # if odd, then grab the middle number
        total = m + n
        med = total // 2

        if (total%2 != 0):
            median = float(lst[med])
            return median
        # if even, then grab the 2 middle point and average it out
        else:
            median = (lst[med] + lst[med -1]) / 2.0
            return median




        