class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        i, j = 0, len(num)-1
        while i <= j:
            if not num[i]+num[j] in ('00', '11', '88', '69', '96'):
                return False
            i += 1
            j -= 1
            continue

        return True