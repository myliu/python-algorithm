class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False

        for prime in [2, 3, 5]:
            while num % prime == 0:
                num /= prime
        return num == 1

if __name__ == '__main__':
    s = Solution()
    print s.isUgly(15)