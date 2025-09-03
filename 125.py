# checkn if a given string is a palindrome, considering only alphanumeric characters and ignoring cases.
# question 125 link: https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        new_char=""
        for char in s:
            if  char.isalpha():
                new_char+=char

        return new_char==new_char[::-1] 

sol=Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))

