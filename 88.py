class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i]=nums2[i]
        return sorted(nums1)
sol=Solution()
print(sol.merge([1,2,3,0,0,0],3,[2,5,6],3))