class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        # 115 ms solution -- O(nlogn)
        # return sorted(num)[len(num)/2]

        # 126 ms solution -- O(n)
        m = num[0]
        count = 1
        for i in range(1, len(num)):
            if count == 0:
                m = num[i]
                count = 1
            elif num[i] == m:
                count += 1
            else:
                count -= 1
        return m

if __name__ == '__main__':
    s = Solution()
    num = [1, 2, 3, 2, 2]
    print s.majorityElement(num)