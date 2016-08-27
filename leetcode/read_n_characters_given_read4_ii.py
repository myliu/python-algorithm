# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):

    def __init__(self):
        self.queue = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while n > 0:
            buf4 = [''] * 4
            read4(buf4)

            self.queue.extend(buf4)
            l = len(self.queue)

            if not l:
                break

            for j in range(min(l, n)):
                buf[i] = self.queue.pop(0)
                i += 1
                n -= 1
        return i