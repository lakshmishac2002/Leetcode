# search insert position
# This is using brute force method
# Time complexity is O(n)
# class Solution:
#     def searchInsert(self, nums: list[int], target: int) -> int:
#         for i in range(len(nums)):
#             if nums[i]>=target:
#                 return i
#         return len(nums)
# sol=Solution()
# print(sol.searchInsert([1,3,5,6],5))

# using binary search
# Time complexity is O(log n)
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
            for i in range(len(nums)):
                left, right = 0, len(nums) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return left
sol=Solution()
print(sol.searchInsert([1,3,5,6],5))
