from collections import Counter, defaultdict

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_counter = Counter(s)
        digit_counter = defaultdict(int)
        for char, count in char_counter.iteritems():
            digit_counter[0] = char_counter['z']
            digit_counter[2] = char_counter['w']
            digit_counter[4] = char_counter['u']
            digit_counter[6] = char_counter['x']
            digit_counter[8] = char_counter['g']
            digit_counter[3] = char_counter['h'] - digit_counter[8]
            digit_counter[5] = char_counter['f'] - digit_counter[4]
            digit_counter[7] = char_counter['s'] - digit_counter[6]
            digit_counter[1] = char_counter['o'] - digit_counter[0] - digit_counter[2] - digit_counter[4]
            digit_counter[9] = char_counter['i'] - digit_counter[5] - digit_counter[6] - digit_counter[8]
        return ''.join(str(digit)*count for digit, count in digit_counter.iteritems())