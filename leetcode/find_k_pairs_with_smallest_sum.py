import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # Create a list of n generators, where n is len(nums1)
        # (x*x for x in range(10)) is the syntax for generator expressions
        # http://anandology.com/python-practice-book/iterators.html#generator-expressions
        streams = map(lambda u: ([u+v, u, v] for v in nums2), nums1)

        # Merge the generators via heapq.merge since each one of them is sorted already
        stream = heapq.merge(*streams)

        return [suv[1:] for suv in heapq.islice(stream, k)]