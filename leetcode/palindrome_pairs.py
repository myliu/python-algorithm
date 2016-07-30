class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        d = {}
        for i, w in enumerate(words):
            d[w] = i

        res = []

        # There are 3 scenarios we need to cover:
        # 1) Classic: ['abc', 'ba']
        # 2) ['ab', 'ba'], we need to ensure no double counts
        # 3) ['aaa'], we need to exclude this case
        for i, w in enumerate(words):
            for j in xrange(len(w)+1):
                prefix = w[:j]
                surfix = w[j:]
                # d[prefix[::-1]] != i and d[surfix[::-1]] != i is to exclude self-palindrome
                if prefix[::-1] in d and surfix == surfix[::-1] and d[prefix[::-1]] != i:
                    res.append([i, d[prefix[::-1]]])
                # j != 0 is to avoid double counts in the case of ['ab', 'ba']
                if j != 0 and surfix[::-1] in d and prefix == prefix[::-1] and d[surfix[::-1]] != i:
                    res.append([d[surfix[::-1]], i])
        return res