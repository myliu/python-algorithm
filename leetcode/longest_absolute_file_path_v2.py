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
            if '.' in path:
                _max = max(_max, paths[depth] + len(path))
            else:
                paths[depth+1] = paths[depth] + len(path) + 1
        return _max