class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = s + '#' + s[::-1]
        failure = [0]
        for i in range(1, len(x)):
            index = failure[i - 1]
            while x[index] != x[i] and index > 0:
                index = failure[index - 1]
            failure.append(index + 1 if x[index] == x[i] else 0)
        return s[failure[-1]:][::-1] + s