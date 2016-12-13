from collections import Counter

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def perm(chars, used, tmp, results):
            if len(tmp) == len(chars):
                results.append(tmp)
                return
            for i in range(len(chars)):
                if used[i]:
                    continue
                if i > 0 and chars[i] == chars[i-1] and not used[i-1]:
                    continue
                used[i] = True
                perm(chars, used, tmp+chars[i], results)
                used[i] = False

        counter = Counter(s)
        chars = []
        mid = ''
        for k, v in counter.items():
            if v % 2 != 0:
                if mid:
                    return []
                mid = k
            chars += [k for _ in range(v/2)]

        used = [False for _ in chars]
        results = []
        perm(chars, used, '', results)
        return [result+mid+result[::-1] for result in results]