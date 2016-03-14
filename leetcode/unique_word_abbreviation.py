import collections

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbr_dict = collections.defaultdict(set)
        for word in dictionary:
            self.abbr_dict[self.abbr(word)].add(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        return len(self.abbr_dict[self.abbr(word)]) == 0 or \
            (len(self.abbr_dict[self.abbr(word)]) == 1 and word in self.abbr_dict[self.abbr(word)])

    def abbr(self, word):
        word_size = len(word)

        if word_size <= 2:
            return word
        else:
            return word[0] + str(word_size-2) + word[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")