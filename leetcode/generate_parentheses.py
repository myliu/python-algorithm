class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.helper(n, n, '', result)
        return result
    
    def helper(self, left, right, tmp, result):
        if left == 0 and right == 0:
            if tmp:
                result += tmp,
            return

        if left > 0:
            self.helper(left-1, right, tmp+'(', result)

        if right > 0 and right > left:
            self.helper(left, right-1, tmp+')', result)

if __name__ == '__main__':
    s = Solution()
    print s.generateParenthesis(3)