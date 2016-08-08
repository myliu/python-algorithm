import collections

# TLE
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []

        if not s or not words:
            return res

        counter = collections.Counter(words)
        wlen = len(words[0])
        wcount = len(words)
        for i in xrange(len(s)-wlen*wcount+1):
            c = counter.copy()
            for j in xrange(len(words)):
                word = s[i+j*wlen:i+j*wlen+wlen]
                if word not in c:
                    break
                else:
                    if c[word] == 1:
                        del c[word]
                    else:
                        c[word] -= 1
                    if not c:
                        res.append(i)
        return res