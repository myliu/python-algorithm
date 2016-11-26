class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        for i in range(1, len(s)+1):
            if s[:i] == s[i-1::-1]:
                for p in self.partition(s[i:]):
                    result += [s[:i]] + p,
        
        if not result:
            return [[]]
        
        return result