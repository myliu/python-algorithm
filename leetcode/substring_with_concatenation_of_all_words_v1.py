import collections

class Solution(object):

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        counter = collections.Counter(words)
        cur_dict = collections.defaultdict(int)
        wlen = len(words[0])
        res = []

        for i in xrange(wlen):
            # cur_dict holds word count in the current window
            cur_dict.clear()
            # count is the word count so far
            count = 0
            # left and right are the index of the window boundary
            left = right = i
            while right + wlen <= len(s):
                word = s[right:right+wlen]
                if word not in counter:
                    cur_dict.clear()
                    count = 0
                    left = right + wlen
                else:
                    cur_dict[word] += 1
                    if cur_dict[word] <= counter[word]:
                        count += 1
                    while cur_dict[word] > counter[word]:
                        tmp = s[left:left+wlen]
                        cur_dict[tmp] -= 1
                        if cur_dict[tmp] < counter[tmp]:
                            count -= 1
                        left += wlen
                    if count == len(words):
                        res.append(left)
                        tmp = s[left:left+wlen]
                        cur_dict[tmp] -= 1
                        count -= 1
                        left += wlen
                right += wlen
        return res