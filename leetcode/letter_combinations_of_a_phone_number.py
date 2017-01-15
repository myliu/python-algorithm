class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        def dfs(digits, start, tmp, results):
            if start == len(digits):
                if tmp:
                    results += tmp,
                return

            for c in mapping[int(digits[start])]:
                dfs(digits, start+1, tmp+c, results)

        results = []
        dfs(digits, 0, '', results)
        return results