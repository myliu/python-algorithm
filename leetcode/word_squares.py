from collections import defaultdict

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        n = len(words[0])

        # Build Prefix Map
        # Key: prefix (from length 0 to length n-1)
        # Value: word
        prefix_map = defaultdict(list)
        for word in words:
            for i in range(1, n):
                prefix_map[word[:i]] += word,

        def build(square, squares):
            if len(square) == n:
                squares += square,
                return

            columns = zip(*square)
            prefix = ''.join(columns[len(square)])
            for word in prefix_map[prefix]:
                build(square + [word], squares)

        squares = []
        for word in words:
            build([word], squares)
        return squares