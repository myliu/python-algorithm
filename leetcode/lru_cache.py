class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity


    def get(self, key):
        """
        :rtype: int
        """
        cache, head, tail = self.cache, self.head, self.tail

        if key not in cache:
            return -1

        node = cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.move_to_tail(node)
        return node.value


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        cache, head, tail = self.cache, self.head, self.tail

        if self.get(key) != -1:
            cache[key].value = value
            return

        if len(cache) >= self.capacity:
            del cache[head.next.key]
            head.next.next.prev = head
            head.next = head.next.next

        current = Node(key, value)
        cache[key] = current
        self.move_to_tail(current)

    
    def move_to_tail(self, node):
        head, tail = self.head, self.tail

        tail.prev.next = node
        node.prev = tail.prev
        node.next = tail
        tail.prev = node


class Node(object):

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None