class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        # number of '1' bits
        k = 0

        while n != 0:
            if n % 2 == 1:
                k = k + 1
            n /= 2
            print 'k: ' + str(k)
            print 'm: ' + str(n)

        return k

if __name__ == '__main__':
    s = Solution()
    print s.hammingWeight(0)