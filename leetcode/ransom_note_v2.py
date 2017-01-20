from collections import defaultdict

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        paper_dict = defaultdict(int)

        for r in magazine:
            paper_dict[r] += 1

        for word in ransomNote:
            paper_dict[word] -= 1

            if paper_dict[word] < 0:
                return False

        return True