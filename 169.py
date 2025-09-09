class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return sorted(nums)[len(nums)//2]
sol=Solution()
print(sol.majorityElement([3,2,3,4,2,1,3,3,2,3]))