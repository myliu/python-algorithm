import re

class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        n = len(target)

        # Find the set of diffs
        diffs = {
                    sum(2**i for i, c in enumerate(word) if c != target[i])
                    for word in dictionary if len(word) == n
                }

        if not diffs:
            return str(n)

        # Iterate over all the combinations, and find the abbr that saves the most characters
        bits = max((i for i in range(2**n) if all(i & diff for diff in diffs)),
                   key=lambda bits: sum((bits >> i) & 3 == 0 for i in range(n-1)))

        # Replace the bits with actual characters and '#'
        s = ''.join(target[i] if 2**i & bits else '#' for i in range(n))

        # Replace '#' with number
        return re.sub('#+', lambda m: str(len(m.group())), s)