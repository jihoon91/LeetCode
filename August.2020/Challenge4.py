'''
Power of Four
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Personal challenge:
Implement the solution without loop and recursion

Ex)
Input: 16
Output: true

'''

from math import log

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        num = log(num,4)
        return num - int(num) == 0

