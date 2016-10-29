class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        result = []
        self.helper(digits, '', result, mapping)
        return result

    def helper(self, digits, tmp, result, mapping):
        if not digits:
            if tmp:
                result += tmp,
            return

        for c in mapping[int(digits[0])]:
            self.helper(digits[1:], tmp+c, result, mapping)