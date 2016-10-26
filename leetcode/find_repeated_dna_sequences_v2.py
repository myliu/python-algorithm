class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        seen, repeated = set(), set()
        for i in range(0, n-9):
            seq = s[i:i+10]
            if seq in seen:
                repeated.add(seq)
            seen.add(seq)
        return list(repeated)