class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # Because the index of the word is returned, we need a map to store the word to index mapping
        idx = {}
        for i, w in enumerate(words):
            idx[w] = i

        results = []
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                prefix = word[:j]
                suffix = word[j:]
                # Without idx[prefix[::-1]] != i, self-palindrome like `s` or `aba` would match itself
                if prefix[::-1] in idx and suffix == suffix[::-1] and idx[prefix[::-1]] != i:
                    results += [i, idx[prefix[::-1]]],
                # j != 0 is to avoid the double counting, e.g, `abcd/dcba` should only be counted once
                if suffix[::-1] in idx and prefix == prefix[::-1] and idx[suffix[::-1]] != i and j != 0:
                    results += [idx[suffix[::-1]], i],
        return results