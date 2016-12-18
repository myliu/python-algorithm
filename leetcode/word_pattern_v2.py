class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        lst = str.split(' ')
        return map(pattern.find, pattern) == map(lst.index, lst)