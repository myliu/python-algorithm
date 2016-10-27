class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0

        i, sign, total = 0, '+', 0

        # Remove white space
        while str[i] == ' ' and i < len(str):
            i += 1

        # Determine sign
        if str[i] == '+':
            sign = '+'
            i += 1
        elif str[i] == '-':
            sign = '-'
            i += 1

        while i < len(str):
            # Stop if illegal character is detected
            if not str[i].isdigit():
                break
            
            total = total * 10 + int(str[i])
            i += 1

        if sign == '+':
            return min(total, 2**31-1)
        else:
            return max(-total, -2**31)