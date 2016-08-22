from collections import deque, defaultdict
from string import ascii_lowercase

class Solution(object):

    def __init__(self):
        self.adjacency_map = defaultdict(list)
        self.results = []

    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        # First, BFS to build an adjacency map
        # Second, DFS to output all the solutions
        ladder = defaultdict(lambda: float('inf'))
        ladder[beginWord] = 0

        min_step = float('inf')
        q = deque()
        q.append(beginWord)
        while q:
            word = q.popleft()
            step = ladder[word] + 1

            if step > min_step:
                break

            for i in range(len(word)):
                for c in ascii_lowercase:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordlist:
                        if step >= ladder[new_word]:
                            continue

                        ladder[new_word] = step
                        self.adjacency_map[new_word].append(word)
                        q.append(new_word)

                        if new_word == endWord:
                            min_step = step

        print ladder
        print self.adjacency_map
        """
        defaultdict(<function <lambda> at 0x1019abd70>, {'hit': 0, 'log': 3, 'dog': 3, 'hot': 1, 'lot': 2, 'dot': 2})
        defaultdict(<type 'list'>, {'log': ['lot'], 'hot': ['hit'], 'lot': ['hot'], 'dot': ['hot'], 'dog': ['dot']})
        """


if __name__ == '__main__':
    s = Solution()
    wordlist = ["hot","dot","dog","lot","log"]
    s.findLadders('hit', 'cog', wordlist)