# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while n > 0:
            buf4 = [''] * 4
            len4 = read4(buf4)
            
            if not len4:
                return i

            for j in range(min(len4, n)):
                buf[i] = buf4[j]
                i += 1
                n -= 1
        return i