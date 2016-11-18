class Solution(object):
    
    def __init__(self):
        self.cache = {}

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        cache = self.cache

        if s in wordDict:
            return True

        if s in cache:
            return cache[s]

        for i in range(1, len(s)):
            if s[:i] in wordDict and self.wordBreak(s[i:], wordDict):
                cache[s] = True
                return True
        cache[s] = False
        return False

if __name__ == '__main__':
    # Initialize Solution object
    s = Solution()

    # Initialize dictionary
    d = set(['hot', 'dog', 'cat', 'aaaa', 'aaa'])

    # Positive test case
    print 'true' if s.wordBreak('hotdog', d) else 'false'
    print 'true' if s.wordBreak('aaaaaaa', d) else 'false'

    # Negative test case
    print 'true' if s.wordBreak('hotpig', d) else 'false'