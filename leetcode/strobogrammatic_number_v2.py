class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        d = { 
              '0': '0',
              '1': '1',
              '8': '8',
              '6': '9',
              '9': '6' 
            }

        n = len(num)
        for i in range(n/2+1):
            if num[i] not in d or d[num[i]] != num[n-1-i]:
                return False
        return True