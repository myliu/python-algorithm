from collections import defaultdict

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.d = defaultdict(set)
        for word in dictionary:
            abbr = self.abbr(word)
            self.d[abbr].add(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = self.abbr(word)
        return len(self.d[abbr]) == 0 or (len(self.d[abbr]) == 1 and word in self.d[abbr])

    def abbr(self, word):
        return word[0] + str(len(word[1:-1])) + word[-1] if len(word) > 2 else word

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")