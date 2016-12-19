class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d, s = dict(), set()
        return self.is_match(pattern, 0, str, 0, d, s)

    def is_match(self, pattern, i, string, j, d, s):
        if i >= len(pattern) and j >= len(string):
            return True
        elif i >= len(pattern) and j < len(string):
            return False
        elif i < len(pattern) and j >= len(string):
            return False

        next_pattern = pattern[i]
        if next_pattern in d:
            next_word = d[next_pattern]
            if not string[j:].startswith(next_word):
                return False
            return self.is_match(pattern, i+1, string, j+len(next_word), d, s)

        for k in range(len(string)-j):
            next_word = string[j:j+k+1]

            if next_word in s:
                continue

            s.add(next_word)
            d[next_pattern] = next_word
            if self.is_match(pattern, i+1, string, j+k+1, d, s):
                return True
            s.remove(next_word)
            del d[next_pattern]

        return False