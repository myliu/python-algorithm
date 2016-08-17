class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # res: list holding the final result
        # cur: list holding the current line result
        # length: total number of characters on the current line
        res, cur, length = [], [], 0
        for w in words:
            if length + len(cur) + len(w) > maxWidth:
                for i in range(maxWidth - length):
                    cur[i % (len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, length = [], 0
            cur.append(w)
            length += len(w)
        res.append(' '.join(cur).ljust(maxWidth))
        return res