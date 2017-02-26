from heapq import *

A = [(1,2), (5,6)]
B = [(1,3)]
C = [(4,10)]

def free_time(matrix):
    heap = []
    for intervals in matrix:
        for start, end in intervals:
            heappush(heap, (start, False)) # enter
            heappush(heap, (end, True)) # exit

    results = []
    count = 0
    prev = None
    while heap:
        interval = heappop(heap)
        # enter
        if not interval[1]:
            if not count and prev:
                results += (prev, interval[0]),
            count += 1
        # exit
        else:
            prev = interval[0]
            count -= 1

    return results

matrix = [A, B, C]
print free_time(matrix)
