#You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order.
#  The large integer does not contain any leading 0's.
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n=len(digits)
        for i in range(n-1,-1,-1):
            if digits[i]<9:
                digits[i]=digits[i]+1
                return digits
            digits[i]=0
        return [1]+digits
sol=Solution()
print(sol.plusOne([9,9,9]))