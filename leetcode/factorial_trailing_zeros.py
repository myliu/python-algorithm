import math

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        m = 0
        i = 1
        while int(math.pow(5, i)) <= n:
            m += n/int(math.pow(5, i))
            i += 1
        return m


if __name__ == '__main__':
    s = Solution()
    print s.trailingZeroes(25)