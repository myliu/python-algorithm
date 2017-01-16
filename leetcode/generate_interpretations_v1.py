class Solution(object):

    def generate_interpretations(self, s):
        def interpret(s):
            c = chr(int(s) - 1 + ord('A'))
            if 'A' <= c <= 'Z':
                return c
            return None

        def helper(s, start, tmp, result):
            if start >= len(s):
                if tmp:
                    result += tmp,
                    return result

            helper(s, start+1, tmp+interpret(s[start]), result)

            if start + 1 < len(s):
                two = interpret(s[start:start+2])
                if two:
                    helper(s, start+2, tmp+two, result)

        result = []
        helper(s, 0, '', result)
        return result


if __name__ == '__main__':
    solution = Solution()
    s = '6121'
    print solution.generate_interpretations(s)