class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        """
        >>> digits = [1, 2, 3]
        >>> map(str, digits)
        ['1', '2', '3']
        >>> ''.join(map(str, digits))
        '123'
        >>> int(''.join(map(str, digits)), 10)
        123
        >>> int(''.join(map(str, digits)), 10) + 1
        124
        >>> str(int(''.join(map(str, digits)), 10) + 1)
        '124'
        >>> map(int, str(int(''.join(map(str, digits)), 10) + 1))
        [1, 2, 4]
        """
        return map(int, str(int(''.join(map(str, digits)), 10) + 1))