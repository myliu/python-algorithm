import heapq

class QueueItem(object):
    def __init__(self, l):
        self.__list = l
        self.__index = 0
        self.__next = self.__list[self.__index]

    def __len__(self):
        return len(self.__list) - self.__index

    def __cmp__(self, other):
        return cmp(self.peek(), other.peek())

    def peek(self):
        return self.__next

    def poll(self):
        ret = self.__next
        self.__index += 1
        if len(self) > 0:
            self.__next = self.__list[self.__index]
        return ret

def merge_k_lists(lists):
    heap = [QueueItem(l) for l in lists]
    heapq.heapify(heap)
    while len(heap) > 0:
        item = heapq.heappop(heap)
        yield item.poll()
        if len(item) > 0:
            heapq.heappush(heap, item)