class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def helper(n, repeats):
            if n in repeats:
                return False

            li = map(int, str(n))
            num = sum(map(lambda x:x**2, li))
            if num == 1:
                return True
            repeats.add(n)
            return helper(num, repeats)

        return helper(n, set())