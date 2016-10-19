import re

class Solution(object):

    def __init__(self):
        self.pattern = re.compile(r'^[+-]?((\.\d+)|(\d+(\.\d*)?))([Ee][+-]?\d+)?$')

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return bool(self.pattern.match(s.strip()))

if __name__ == '__main__':
    s = Solution()
    print s.isNumber('+1')
    print s.isNumber('.123')
    print s.isNumber('0.123')
    print s.isNumber('123')
    print s.isNumber('e6')