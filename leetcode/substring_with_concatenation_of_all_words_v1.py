import collections

class Solution(object):

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        counter = collections.Counter(words)
        window = collections.defaultdict(int)
        _len = len(words[0])
        result = []

        for i in range(_len):
            # Left and right are the index of the window boundary
            left = right = i
            # Window holds word count in the current window
            window.clear()
            # Count is the word count so far
            count = 0
            while right + _len <= len(s):
                word = s[right:right+_len]
                if word not in counter:
                    window.clear()
                    count = 0
                    left = right + _len
                else:
                    window[word] += 1
                    if window[word] <= counter[word]:
                        count += 1
                    while window[word] > counter[word]:
                        tmp = s[left:left+_len]
                        window[tmp] -= 1
                        if window[tmp] < counter[tmp]:
                            count -= 1
                        left += _len
                    if count == len(words):
                        result += left,
                        tmp = s[left:left+_len]
                        window[tmp] -= 1
                        count -= 1
                        left += _len
                right += _len
        return result

if __name__ == '__main__':
    s = Solution()
    print s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])