import collections

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern_dict = collections.defaultdict(list)
        for i in range(len(pattern)):
            pattern_dict[pattern[i]].append(i)

        word_dict = collections.defaultdict(list)
        words = str.split()
        for i in range(len(words)):
            word_dict[words[i]].append(i)

        if sorted(pattern_dict.values()) == sorted(word_dict.values()):
            return True
        return False