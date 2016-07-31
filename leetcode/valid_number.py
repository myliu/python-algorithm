class Solution(object):
    regex = re.compile(r'^[+-]?((\d*\.\d+)|(\d+(\.\d*)?))([eE][+-]?\d+)?$')

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return bool(self.regex.match(s.strip()))