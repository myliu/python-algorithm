# KMP-based
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = s + '#' + s[::-1]
        print x
        failure = [0]
        for i in range(1, len(x)):
            index = failure[i - 1]
            while x[index] != x[i] and index > 0:
                index = failure[index - 1]
            failure.append(index + 1 if x[index] == x[i] else 0)
            print failure
        return s[failure[-1]:][::-1] + s

"""
cdcba#abcdc
[0, 0]
[0, 0, 1]
[0, 0, 1, 0]
[0, 0, 1, 0, 0]
[0, 0, 1, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0, 1]
[0, 0, 1, 0, 0, 0, 0, 0, 1, 2]
[0, 0, 1, 0, 0, 0, 0, 0, 1, 2, 3]
abcdcba
"""
if __name__ == '__main__':
    s = Solution()
    print s.shortestPalindrome("cdcba")