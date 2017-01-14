class CountInterpretations(object):
    
    def count(self, s):
        if not s:
            return 1

        if s[0] == '0':
            return 0

        if len(s) == 1:
            return 1

        count = 0
        if int(s[0]) > 0:
            count += self.count(s[1:])

        if int(s[:2]) <= 26:
            count += self.count(s[2:])

        return count

if __name__ == '__main__':
    counter = CountInterpretations()
    print counter.count('11')
    print counter.count('111')