class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper(word, pos, tmp, count, result):
            if pos == len(word):
                # Once we reach the end, append tmp to the result
                result += tmp + (str(count) if count > 0 else ''),
            else:
                # Skip current position, and increment count
                helper(word, pos + 1, tmp, count + 1, result)
                # Include current position, and zero-out count
                helper(word, pos + 1, tmp + (str(count) if count > 0 else '') + word[pos], 0, result)

        result = []
        helper(word, 0, '', 0, result)
        return result