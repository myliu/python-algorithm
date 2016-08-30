class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        self.reverse(s, 0, (len(s)-1))
        start = i = 0
        while i < len(s):
            if s[i] == ' ':
                self.reverse(s, start, i-1)
                start = i + 1
            i += 1
        self.reverse(s, start, (len(s)-1))

    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1