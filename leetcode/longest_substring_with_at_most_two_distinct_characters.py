class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = l = 0
        distinct = {}
        for r, c in enumerate(s):
            if c not in distinct and len(distinct) == 2:
                lowest = min(distinct.values())
                l = lowest + 1
                
                for k, v in distinct.items():
                    if v == lowest:
                        distinct.pop(k)
                        break

            maxlen = max(maxlen, r-l+1)
            distinct[c] = r
        return maxlen