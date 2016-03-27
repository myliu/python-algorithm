class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        def is_match(pattern, i, str, j, d, s):
            if i >= len(pattern) and j >= len(str):
                return True
            elif i >= len(pattern) and j < len(str):
                return False
            elif i < len(pattern) and j >= len(str):
                return False

            next_pattern = pattern[i]
            if next_pattern in d:
                next_word = d[next_pattern]
                if not str.startswith(next_word, j):
                    return False
                return is_match(pattern, i+1, str, j+len(next_word), d, s)

            for k in range(len(str)-j):
                next_word = str[j:j+k+1]

                if next_word in s:
                    continue

                d[next_pattern] = next_word
                s.add(next_word)

                if is_match(pattern, i+1, str, j+len(next_word), d, s):
                    return True

                del d[next_pattern]
                s.remove(next_word)
            return False

        d = {}
        s = set()
        return is_match(pattern, 0, str, 0, d, s)