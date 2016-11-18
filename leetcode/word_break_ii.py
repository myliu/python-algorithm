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

            results = [word + (' ' if result else '') + result
                       for word in wordDict if s.startswith(word)
                       for result in dfs(s[len(word):], wordDict, cache)]

            cache[s] = results
            return results

        return dfs(s, wordDict, {})