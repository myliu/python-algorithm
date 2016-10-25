class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        missing_type = 3
        if any('a' <= ch <= 'z' for ch in s): missing_type -= 1
        if any('A' <= ch <= 'Z' for ch in s): missing_type -= 1
        if any(ch.isdigit() for ch in s): missing_type -= 1

        """
        For the repeating sequence, 
        'one' means one deletion can reduce one replacement of the repeating sequence.
        'two' means two deletion can reduce one replacement of the repeating sequence.
        """
        one = two = replacements = 0
        i = 2
        while i < len(s):
            if s[i] == s[i-1] == s[i-2]:
                repeats = 2
                while i < len(s) and s[i] == s[i-1]:
                    repeats += 1
                    i += 1

                # End of current repeat
                replacements += repeats / 3
                one += repeats % 3 == 0
                two += repeats % 3 == 1
            else:
                i += 1

        if len(s) < 6:
            return max(missing_type, 6 - len(s))
        elif len(s) <= 20:
            return max(missing_type, replacements)
        else:
            deletions = len(s) - 20

            replacements -= min(deletions, one)
            replacements -= min(max(deletions - one, 0), two * 2) / 2
            replacements -= max(deletions - one - two * 2, 0) / 3
            return deletions + max(missing_type, replacements)