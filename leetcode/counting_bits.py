class Solution(object):

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def count1s(num):
            k = 0
            while num != 0:
                if num in d:
                    return d[num]

                if num % 2 == 1:
                    k += 1
                num /= 2
            d[num] = k
            return k

        d = {}
        return [count1s(i) for i in range(num+1)]