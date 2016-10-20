class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        paths = {0:0}
        lines = input.splitlines()

        _max = 0
        for line in lines:
            path = line.lstrip('\t')
            depth = len(line) - len(path)
            paths[depth] = paths[depth-1] + len(path) + 1 if depth else len(path)
            if '.' in path:
                _max = max(_max, paths[depth])
        return _max