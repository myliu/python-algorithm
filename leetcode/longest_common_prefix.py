class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        for col in zip(*strs):
            if any(i != col[0] for i in col):
                return prefix
            prefix += col[0]
        return prefix