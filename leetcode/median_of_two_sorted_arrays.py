class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n % 2 == 0:
            # Return float, thus 2.0
            return (self.find_kth(nums1, 0, nums2, 0, n/2) + self.find_kth(nums1, 0, nums2, 0, n/2+1)) / 2.0
        else:
            return self.find_kth(nums1, 0, nums2, 0, n/2+1)

    """
    The idea is that at each iteration, we reduce k by k/2.
    Thus, we have call like self.find_kth(nums1, start1 + k/2, nums2, start2, k - k/2)
    In order to determine which part to discard, we should compare nums1[start1 + k/2 - 1].
    """
    def find_kth(self, nums1, start1, nums2, start2, k):
            if start1 == len(nums1):
                print start1
                print 'if start1 == len(nums1): ' + str(nums2[start2+k-1])
                return nums2[start2+k-1]

            if start2 == len(nums2):
                print start2
                print 'if start2 == len(nums2): ' + str(nums1[start1+k-1])
                return nums1[start1+k-1]

            if k == 1:
                print 'if k==1 find_kth: ' + str(min(nums1[start1], nums2[start2]))
                return min(nums1[start1], nums2[start2])

            discard1 = nums1[start1 + k/2 - 1] if start1 + k/2 - 1 < len(nums1) else float('inf')
            discard2 = nums2[start2 + k/2 - 1] if start2 + k/2 - 1 < len(nums2) else float('inf')

            print 'k: ' + str(k)
            print 'discard1: ' + str(discard1)
            print 'discard2: ' + str(discard2)

            if discard1 <= discard2:
                # The last argument should be k - k/2 because k could be odd number, like 5.
                return self.find_kth(nums1, start1 + k/2, nums2, start2, k - k/2)
            else:
                return self.find_kth(nums1, start1, nums2, start2 + k/2, k - k/2)


if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 3, 4, 5]
    B = [6, 7, 8, 9, 10]
    print s.findMedianSortedArrays(A, B)