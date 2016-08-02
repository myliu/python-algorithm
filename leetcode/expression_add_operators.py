class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def helper(num, target, pos, path, val, multiplier, res):
            if pos == len(num):
                if val == target:
                    res.append(path)

            for i in xrange(pos, len(num)):
                if i > pos and num[pos] == '0':
                    break

                current = int(num[pos:i+1])
                if pos == 0:
                    helper(num, target, i+1, str(current), current, current, res)
                else:
                    helper(num, target, i+1, path + '+' + str(current), val + current, current, res)
                    helper(num, target, i+1, path + '-' + str(current), val - current, -current, res)
                    helper(num, target, i+1, path + '*' + str(current), val - multiplier + multiplier * current, multiplier * current, res)

        res = []
        # The initial path, val and multiplier do not matter, and they will be overriden later
        helper(num, target, 0, 'xxx', 888, 999, res)
        return res