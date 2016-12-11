class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        result = []
        for i, c in enumerate(input):
            if c in '+-*':
                for left in self.diffWaysToCompute(input[:i]):
                    for right in self.diffWaysToCompute(input[i+1:]):
                        if c == '+':
                            result += left + right,
                        elif c == '-':
                            result += left - right,
                        else:
                            result += left * right,

        # When there is no '+-*' in the input
        if not result:
            result += int(input),

        return result