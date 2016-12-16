class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result = []
        # The initial path, val and multiplier do not matter, and they will be overriden later
        self.dfs(num, target, 0, '', 0, 0, result)
        return result

    def dfs(self, num, target, pos, path, val, multiplier, result):
        if pos == len(num):
            if val == target:
                result += path,

        for i in xrange(pos, len(num)):
            if i > pos and num[pos] == '0':
                break

            curr = int(num[pos:i+1])
            if pos == 0:
                self.dfs(num, target, i+1, str(curr), curr, curr, result)
            else:
                self.dfs(num, target, i+1, path+'+'+str(curr), val+curr, curr, result)
                self.dfs(num, target, i+1, path+'-'+str(curr), val-curr, -curr, result)
                self.dfs(num, target, i+1, path+'*'+str(curr), val-multiplier+multiplier*curr, multiplier*curr, result)