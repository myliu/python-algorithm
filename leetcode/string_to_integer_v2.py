class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        # Remove white space
        s = s.strip()

        # Determine sign
        sign = '+'
        if s[0] in ('+', '-'):
            if s[0] == '-':
                sign = '-'
            s = s[1:]

        num = 0
        for c in s:
            # Stop if illegal character is detected
            if not c.isdigit():
                break

            num = num * 10 + int(c)

        if sign == '+':
            return min(num, 2**31-1)
        else:
            return max(-num, -2**31)