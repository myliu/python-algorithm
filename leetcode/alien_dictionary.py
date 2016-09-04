from collections import defaultdict, deque

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        orders = defaultdict(set)
        degrees = dict.fromkeys(set(''.join(words)), 0)

        for i in range(len(words)-1):
            current = words[i]
            next = words[i+1]
            length = min(len(current), len(next))
            for j in range(length):
                if current[j] == next[j]:
                    continue
                if next[j] not in orders[current[j]]:
                    orders[current[j]].add(next[j])
                    degrees[next[j]] += 1
                    break

        queue = deque()
        for k, v in degrees.items():
            if not v:
                queue.append(k)

        result = ''
        while queue:
            char = queue.popleft()
            result += char
            tos = orders[char]
            for to in tos:
                degrees[to] -= 1
                if not degrees[to]:
                    queue.append(to)
        return result if len(result) == len(degrees) else ''