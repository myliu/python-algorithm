from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        n = len(secret)

        bulls = 0
        s, g = [], []
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                s += secret[i],
                g += guess[i],

        counter = Counter(s) & Counter(g)
        cows = sum(counter.values())
        return str(bulls) + 'A' + str(cows) + 'B'