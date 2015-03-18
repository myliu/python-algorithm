import sys

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        length = len(A) + len(B)
        if length % 2 == 0:
            return (self.find_Kth(A, 0, B, 0, length/2) + self.find_Kth(A, 0, B, 0, length/2+1)) / 2.0
        else:
            return self.find_Kth(A, 0, B, 0, length/2+1)

    def find_Kth(self, A, A_start, B, B_start, k):
        if A_start >= len(A):
            print A_start
            print 'if A_start >= len(A): ' + str(B[B_start + k - 1])
            return B[B_start + k - 1]

        if B_start >= len(B):
            print B_start
            print 'if B_start >= len(B): ' + str(A[A_start + k - 1])
            return A[A_start + k - 1]

        if k == 1:
            print 'if k==1 find_Kth: ' + str(min(A[A_start], B[B_start]))
            return min(A[A_start], B[B_start])

        A_key = A[A_start + k/2 - 1] if A_start + k/2 - 1 < len(A) else sys.maxint
        B_key = B[B_start + k/2 - 1] if B_start + k/2 - 1 < len(B) else sys.maxint

        print 'k: ' + str(k)
        print 'A Key: ' + str(A_key)
        print 'B Key: ' + str(B_key)

        if A_key <= B_key:
            return self.find_Kth(A, A_start + k/2, B, B_start, k - k/2)
        else:
            return self.find_Kth(A, A_start, B, B_start + k/2, k - k/2)



if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 3]
    B = [4, 5, 7]
    print s.findMedianSortedArrays(A, B)