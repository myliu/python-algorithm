from heapq import *

class Solution:
    def getSkyline(self, LRH):
        # Priority Queue to store the height and right position of the live buildings
        live_hr = []
        # To store final result
        skyline = []
        i, n = 0, len(LRH)

        while i < n or live_hr:
            if not live_hr or i < n and LRH[i][0] <= -live_hr[0][1]:
                x = LRH[i][0]
                while i < n and LRH[i][0] == x:
                    heappush(live_hr, [-LRH[i][2], -LRH[i][1]])
                    i += 1
            else:
                x = -live_hr[0][1]
                while live_hr and -live_hr[0][1] <= x:
                    heappop(live_hr)
            height = -live_hr[0][0] if live_hr else 0
            if not skyline or height != skyline[-1][1]:
                skyline.append([x, height])
        return skyline

if __name__ == '__main__':
    s = Solution()
    LRH = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]];
    print s.getSkyline(LRH)