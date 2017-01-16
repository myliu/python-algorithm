class Solution(object):

    def _interpret(s, size):
        r = ''
        if size == 1:
            r = s[0] - '1' + 'A'
        elif size == 2:
            r = 'A' + 10 * (s[0] - '1') + (s[1] - '1')

        if r > 'Z' or r < 'A':
            return ''

        return r


    def _prepend(prefix, suffixes, output):
        for suffix in suffixes:
            output += (prefix + suffix),

    def get_interpretations(s):
        outputs = []
        if not s:
            output += '',
            return output

        _prepend(_interpret(s, 1), self.get_interpretations(s[1:]), outputs)