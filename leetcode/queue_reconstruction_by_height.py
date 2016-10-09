class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for p in sorted(people, key=lambda (h, k): (-h, k)):
            result.insert(p[1], p)
        return result