'''
LeetCode problem 520.
Detect capital
Use detect method, isupper() only once.
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