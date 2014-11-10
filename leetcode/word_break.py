class Solution:

    def __init__(self):
        self.cache = {}

    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if s in dict:
            return True

        if s in self.cache:
            return self.cache[s]

        for i in range(len(s)):
            if s[:i+1] in dict:
                if self.wordBreak(s[i+1:], dict):
                    self.cache[s] = True
                    return True
        self.cache[s] = False
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