from collections import Counter

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        counter = Counter(s)
        odd = 0
        mid = ''
        for k, v in counter.items():
            if v % 2 == 1:
                odd += 1
                mid = k
            if odd > 1:
                return []

        counter -= Counter(mid)
        chars = sorted(counter.elements())[::2]
        result = []
        self.dfs(chars, '', result)
        return [s + mid + s[::-1] for s in result] if result else [mid]

    def dfs(self, chars, tmp, result):
        if not chars:
            if tmp:
                result += tmp,
            return

        for i in range(len(chars)):
            if i > 0 and chars[i] == chars[i-1]:
                continue
            self.dfs(chars[:i]+chars[i+1:], tmp+chars[i], result)