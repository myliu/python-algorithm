class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        str.split([sep[, maxsplit]])
        If sep is not specified or is None, a different splitting algorithm is applied:
        runs of consecutive whitespace are regarded as a single separator,
        and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace.
        Consequently, splitting an empty string or a string consisting of just whitespace with a None separator returns [].
        """
        return ' '.join(s.split()[::-1])