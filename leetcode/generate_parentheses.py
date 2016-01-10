class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.helper(result, '', n, n)
        return result

    def helper(self, result, current, left, right):
        if left == 0 and right == 0:
            result.append(current)
            return

        if left > 0:
            self.helper(result, current + '(', left - 1, right)

        if right > 0 and right > left:
            self.helper(result, current + ')', left, right - 1)

if __name__ == '__main__':
    s = Solution()
    print s.generateParenthesis(3)