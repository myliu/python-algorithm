class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        def dfs(s, wordDict, cache):
            if s in cache:
                return cache[s]

            if not s:
                return ['']

            results = []
            for word in wordDict:
                if s.startswith(word):
                    for r in dfs(s[len(word):], wordDict, cache):
                        result = word + (' ' if r else '') + r
                        results.append(result)
            cache[s] = results
            return results

        return dfs(s, wordDict, {})