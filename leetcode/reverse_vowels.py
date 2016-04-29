import re

class Solution(object):
    def reverseVowels(self, s):
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

s = 'leetcode'
solution = Solution()
print solution.reverseVowels(s)