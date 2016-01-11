from collections import defaultdict

class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.d = defaultdict(int)
        

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.d[number] += 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        d = self.d
        return any(value-num in d and (value-num != num or d[num] > 1) for num in d)

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)