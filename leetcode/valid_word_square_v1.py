class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        n = max(len(word) for word in words)
        columns = ['' for _ in range(n)]
        for word in words:
            for i, c in enumerate(word):
                columns[i] += c
        return words == columns