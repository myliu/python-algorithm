from collections import defaultdict

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for string in strings:
            s = ''
            diff = ord(string[0]) - ord('a')
            for c in string:
                normalized = ord(c) - diff
                if normalized < ord('a'):
                    normalized += 26
                s += chr(normalized)
            d[s] += string,
        return d.values()