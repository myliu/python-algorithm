class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return [left + right if c == '+' else left - right if c == '-' else left * right
                for i, c in enumerate(input) if c in '+-*'
                for left in self.diffWaysToCompute(input[:i])
                for right in self.diffWaysToCompute(input[i+1:])] or [int(input)]