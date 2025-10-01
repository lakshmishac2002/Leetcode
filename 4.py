# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        for i in range(n):
            nums1.append(nums2[i])
        nums1.sort()
        m=len(nums1)
        if m%2==1:
            return (nums1[m//2])
        else:
            mid1=m//2
            mid2=(m//2)-1
            return (nums1[mid1]+nums1[mid2])/2
sol=Solution()
print(sol.findMedianSortedArrays([1,3],[2,4]))
        