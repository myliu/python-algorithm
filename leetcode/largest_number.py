class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        # Same as:
        # c = lambda x, y: cmp(x+y, y+x)
        c = lambda x, y: 1 if x+y > y+x else -1 if y+x > x+y else 0
        num = map(str, num)
        num.sort(cmp=c, reverse=True)
        # Cast to int, then cast back to str is to remove leading 0s
        return str(int("".join(num)))

if __name__ == '__main__':
    s = Solution()
    num = [0, 0]
    # num = [3, 30, 34, 5, 9]
    print s.largestNumber(num)