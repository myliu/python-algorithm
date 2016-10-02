from collections import defaultdict
from random import choice

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        nums, pos = self.nums, self.pos
        nums.append(val)
        pos[val].add(len(nums)-1)
        return len(pos[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        nums, pos = self.nums, self.pos
        if pos[val]:
            idx, last = pos[val].pop(), nums[-1]
            nums[idx] = last
            pos[last].add(idx)
            pos[last].discard(len(nums)-1)
            nums.pop()
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return choice(self.nums)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()