#Length of Last Word
#Given a string s consisting of words and spaces, return the length of the last word in the string.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        return len(s[-1])
sol=Solution()
print(sol.lengthOfLastWord("Hello World"))
        