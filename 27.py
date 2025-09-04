# Remove element
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
#using pop method but this time complexity can go upto O(n^2)
        # for i in range(len(nums)-1,-1,-1):
        #     if nums[i]==val:
        #         nums.pop(i)
        # return len(nums)

# Best approach is using pointer
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k
sol=Solution()
print(sol.removeElement([3,2,3,2],3))