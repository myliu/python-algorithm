class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    # Three step to reverse.
    def reverseWords(self, s):
        n = len(s)

        # 1. Reverse the whole sentence.
        self.reverse(s, 0, n-1)

        # 2. Reverse each word.
        start = i = 0
        while i < n:
            if s[i] == ' ':
                self.reverse(s, start, i-1)
                start = i + 1
            i += 1

        # 3. Reverse the last word, if there is only one word this will solve the corner case.
        self.reverse(s, start, n-1)

    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1