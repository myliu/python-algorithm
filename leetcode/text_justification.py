class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # results: list holding the final result
        # current: list holding the current line result
        # length: total number of characters on the current line
        length, current, results = 0, [], []
        for word in words:
            if length + len(current) + len(word) > maxWidth:
                for i in range(maxWidth - length):
                    # or 1 is to deal with the case where len(current) is 1
                    current[i % (len(current) - 1 or 1)] += ' '
                results += ''.join(current),
                length, current = 0, []
            length += len(word)
            current += word,

        # Deal with the last line
        results += ' '.join(current).ljust(maxWidth),
        return results

if __name__ == '__main__':
    s = Solution()
    print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)