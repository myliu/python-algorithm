class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        values = [0 for _ in range(n)]
        for i in range(n):
            word = words[i]
            for j in range(len(word)):
                values[i] |= 1 << (ord(word[j])-ord('a'))

        max_product = 0
        for i in range(n):
            for j in range(i+1, n):
                if values[i] & values[j] == 0 and len(words[i]) * len(words[j]) > max_product:
                    max_product = len(words[i]) * len(words[j])
        return max_product