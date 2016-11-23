from string import ascii_lowercase

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        set1 = {beginWord}
        set2 = {endWord}
        return self.bfs(set1, set2, wordList, 1)

    def bfs(self, set1, set2, words, level):
        if not set1:
            return 0

        if len(set1) > len(set2):
            return self.bfs(set2, set1, words, level)

        for word in set1:
            if word in words:
                words.remove(word)

        for word in set2:
            if word in words:
                words.remove(word)

        set3 = set()
        for word in set1:
            for i in range(len(word)):
                for c in ascii_lowercase:
                    tmp = word[:i] + c + word[i+1:]

                    if tmp in set2:
                        return level + 1

                    if tmp in words:
                        set3.add(tmp)

        return self.bfs(set2, set3, words, level+1)