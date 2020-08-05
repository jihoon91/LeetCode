'''
Design HashSet
Design a HashSet without using any built-in hash table libraries.
To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Condition:
1. All values will be in the range of [0, 1000000].
2. The number of operations will be in the range of [1, 10000].
3. Please do not use the built-in HashSet library.
'''

class MyHashSet: 
    def eval_hash(self, key):
        return ((key*1000007) & (1<<22) - 1)>>8 #Condition.1 , Shift left by 22 bits - 1, then Shift right by 8 bits
                                                 
    def __init__(self):
        self.arr = [[] for _ in range(1<<14)] #Condition.2 , Shift left by 14 bits (2^14 = 16384 > 10000)

    def add(self, key: int) -> None:
        t = self.eval_hash(key)
        if key not in self.arr[t]:
            self.arr[t].append(key)

    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        if key in self.arr[t]:
            self.arr[t].remove(key)

    def contains(self, key: int) -> bool:
        t = self.eval_hash(key)
        return key in self.arr[t]

