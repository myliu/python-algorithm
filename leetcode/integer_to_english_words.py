class Solution(object):
    
    LESS_THAN_20 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    TENS = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    THOUSANDS = ['', 'Thousand', 'Million', 'Billion']

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        # helper always add trailing space
        def helper(num):
            if num == 0:
                return ''
            elif num < 20:
                return self.LESS_THAN_20[num] + ' '
            elif num < 100:
                return self.TENS[num/10] + ' ' + helper(num%10)
            else:
                return self.LESS_THAN_20[num/100] + ' Hundred ' + helper(num%100)

        words = ''
        i = 0

        if num == 0:
            return 'Zero'

        while num > 0:
            if num % 1000:
                words = helper(num % 1000) + self.THOUSANDS[i] + ' ' + words
            num /= 1000
            i += 1

        return words.strip()