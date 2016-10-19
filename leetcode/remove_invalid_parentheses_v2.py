class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def validate(s):
            count = 0
            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    if count == 0:
                        return False
                    count -= 1
            return count == 0

        def helper(level):
            valid = filter(validate, level)
            if valid:
                return valid
            return helper({s[:i]+s[i+1:] for s in level for i in range(len(s))})
            
        return helper({s})