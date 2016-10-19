public class LRUCache {

    private Map<Integer, Node> map = new HashMap<Integer, Node>();
    private int capacity;
    // Head node is the least recently used element
    private Node head = new Node(-1, -1);
    // Tail node is the most recently used element
    private Node tail = new Node(-1, -1);

    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        // Cache miss
        if (!map.containsKey(key)) {
            return -1;
        }

        // Cache hit
        Node current = map.get(key);

        // Remove current element, and move it to tail
        current.prev.next = current.next;
        current.next.prev = current.prev;
        moveToTail(current);
        return current.value;
    }

    public void set(int key, int value) {
        // Update existing element in the cache
        // 1) Move the element to tail in Doubly linked list
        // 2) Update HashMap
        if (get(key) != -1) {
            map.get(key).value = value;
            return;
        }

        if (map.size() == capacity) {
            // Remove least recently used element from head
            map.remove(head.next.key);
            head.next = head.next.next;
            head.next.prev = head;
        }

        // Add new element to the tail
        Node current = new Node(key, value);
        map.put(key, current);
        moveToTail(current);
    }

    void moveToTail(Node current) {
        tail.prev.next = current;
        current.prev = tail.prev;
        current.next = tail;
        tail.prev = current;
    }

    private class Node {
        Node prev;
        Node next;
        Integer key;
        Integer value;
        
        public Node(Integer key, Integer value) {
            this.prev = null;
            this.next = null;
            this.key = key;
            this.value = value;
        }
    }
}