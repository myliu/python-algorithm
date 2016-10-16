class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        grid = map(None, *words)
        return grid == map(None, *grid)