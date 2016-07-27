class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def helper(digits, tmp, mapping, res):
            if not digits:
                if tmp:
                    res.append(tmp)
                return
            for i in list(mapping[int(digits[0])]):
                helper(digits[1:], tmp + i, mapping, res)

        mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        helper(digits, '', mapping, res)
        return res