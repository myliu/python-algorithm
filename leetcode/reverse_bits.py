class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # Integer to be returned
        m = 0

        # Number of digits
        k = 0

        while n != 0:
            if n % 2 == 1:
                m = m * 2 + 1
            else:
                m <<= 1
            n /= 2
            k += 1
            print 'm: ' + str(m)
            print 'n: ' + str(n)
            print 'k: ' + str(k)

        for i in range(32-k):
            m <<= 1

        return m

if __name__ == '__main__':
    s = Solution()
    print s.reverseBits(43261596)