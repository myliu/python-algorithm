class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        string = list(s)
        left, right = 0, len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        while left < right:
            if string[left].lower() in vowels and string[right].lower() in vowels:
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1
            else:
                if string[left].lower() not in vowels:
                    left += 1
                if string[right].lower() not in vowels:
                    right -= 1
        return ''.join(string)