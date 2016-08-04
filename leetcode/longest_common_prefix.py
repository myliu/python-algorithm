class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        tmp = []
        for x in zip(*strs):
            if all(y == x[0] for y in x):
                tmp.append(x[0])
            else:
                break
        return ''.join(tmp)