class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        minimum = float('-inf')
        stack = []
        for n in preorder:
            if n < minimum:
                return False
            while stack and stack[-1] < n:
                minimum = stack.pop()
            stack.append(n)
        return True
        
"""
Input: [5,3,1,4,8,7,6,9]
At a given point, the "minimum" that just got popped is the root node
For example, when we see 8, 5 got popped (5 is the root node)
We cannot add any value smaller than 5 once 5 got popped
The entire left tree of 5 should already be gone
"""