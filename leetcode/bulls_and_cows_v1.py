from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s, g = Counter(secret), Counter(guess)
        A = sum(i == j for i, j in zip(secret, guess))
        B = sum((s&g).values()) - A
        return str(A) + 'A' + str(B) + 'B'