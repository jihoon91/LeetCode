'''
Detect capital
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

Personal Challenge:
Use detect method, isupper(), only once.
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        size = len(word)
        if size == 1:
            return True
        countchange=0
        tmp =[]
        for i in range(size):
            if word[i].isupper():
                tmp.append(1)
            else:
                tmp.append(0) 
            if i >0 and tmp[i-1] != tmp[i]:
                countchange += 1 
            if countchange > 1:
                return False
        
        if countchange == 0 or (tmp[0] == 1 and sum(tmp) == 1):
            return True
        return False