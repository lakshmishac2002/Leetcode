# Square of a Sorted Array
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            return sorted([nums[i]**2 for i in range(len(nums))])
sol=Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))