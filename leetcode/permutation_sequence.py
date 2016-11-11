from math import factorial

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in range(1, n+1)]
        permutation = ''

        # Convert from Ordinal to Cardinal number
        k -= 1

        # Iterate n times, and the length of 'permutation' increases by 1 in each iteration
        while n > 0:
            n -= 1
            current, k = divmod(k, factorial(n))
            permutation += nums[current]
            nums.remove(nums[current])
        return permutation

if __name__ == '__main__':
    s = Solution()
    print s.getPermutation(4, 7)