class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newnum = nums1 + nums2
        newnum.sort()
        median = 0

        l , r = 0, len(newnum)-1
        while l <= r:
            m = (l + r)//2
            if len(newnum) % 2 == 0:
                median = (newnum[m] + newnum[m+1])/2
                return median
            if len(newnum) % 2 == 1:
                median = newnum[m]
                return median
