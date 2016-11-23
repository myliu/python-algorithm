from collections import deque, defaultdict
from string import ascii_lowercase

class Solution(object):

    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        # First, BFS to build an adjacency map
        # Second, DFS to output all the solutions
        if not wordlist:
            return []

        wordlist.add(endWord)

        adjacency_map = defaultdict(set)

        ladder = defaultdict(lambda: float('inf'))
        ladder[beginWord] = 0

        # min_step is important here since it is possible there are multiple solutions
        min_step = float('inf')

        q = deque()
        q += beginWord,
        while q:
            word = q.popleft()
            step = ladder[word] + 1

            if step > min_step:
                break

            for i in range(len(word)):
                for c in ascii_lowercase:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordlist:
                        if step > ladder[new_word]:
                            continue

                        if step < ladder[new_word]:
                            ladder[new_word] = step
                            q.append(new_word)

                        """
                        ["hit","hot","dot","dog","cog"]
                        ["hit","hot","lot","log","cog"]
                        When we reach "cog" for the second time, step is the same as ladder[new_word].
                        """

                        adjacency_map[word].add(new_word)

                        if new_word == endWord:
                            min_step = step

        results = []
        self.dfs(beginWord, endWord, [], results, adjacency_map)
        return results

    def dfs(self, begin, end, tmp, results, adjacency_map):
        if begin == end:
            results += tmp + [end],
            return

        for new_begin in adjacency_map[begin]:
            self.dfs(new_begin, end, tmp + [begin], results, adjacency_map)


if __name__ == '__main__':
    s = Solution()
    wordlist = set(["hot","dot","dog","lot","log"])
    print s.findLadders('hit', 'cog', wordlist)