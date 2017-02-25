from collections import defaultdict, deque

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        orders = defaultdict(set)
        degrees = {}
        for c in set(''.join(words)):
            degrees[c] = 0

        for i in range(len(words)-1):
            curr = words[i]
            _next = words[i+1]
            length = min(len(curr), len(_next))
            for j in range(length):
                if curr[j] == _next[j]:
                    continue
                if _next[j] not in orders[curr[j]]:
                    orders[curr[j]].add(_next[j])
                    degrees[_next[j]] += 1
                # The loop need to be broken anyway if curr[j] != _next[j]
                break

        queue = deque()
        for k, v in degrees.items():
            if not v:
                queue += k,

        result = ''
        while queue:
            curr = queue.popleft()
            result += curr
            _next = orders[curr]
            for c in _next:
                degrees[c] -= 1
                if not degrees[c]:
                    queue += c,
        return result if len(result) == len(degrees) else ''