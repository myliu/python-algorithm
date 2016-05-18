class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper(word, pos, cur, count, result):
            if len(word) == pos:
                result.append(cur + str(count) if count > 0 else cur)
            else:
                helper(word, pos + 1, cur, count + 1, result)
                helper(word, pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0, result)

        result = []
        helper(word, 0, '', 0, result)
        return result