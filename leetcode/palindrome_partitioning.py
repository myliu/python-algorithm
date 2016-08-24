class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        results = []
        for i in range(1, len(s)+1):
            if s[:i] == s[i-1::-1]:
                for rest in self.partition(s[i:]):
                    results.append([s[:i]] + rest)

        if not results:
            return[[]]

        return results