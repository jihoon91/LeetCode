'''
Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
EX)
Input: "A man, a plan, a canal: Panama"
Output: true
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        tmp = ""
        for t in s:
            if t.isalpha():
                tmp += t.upper()
            elif t.isnumeric():
                tmp += t
        size = len(tmp)
        for i in range(size//2):
            if tmp[i]!=tmp[-i-1]:
                return False
        return True