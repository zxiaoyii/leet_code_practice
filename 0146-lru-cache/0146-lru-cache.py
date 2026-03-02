class ListNode:
    def __init__(self, key = 0, val = 0):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> nodes
        self.start = ListNode()
        self.end = ListNode()
        self.start.next = self.end
        self.end.prev = self.start

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # delete node
            self.deleteNodeFromLinkedList(node)
            # move node to the most recent
            self.moveToFrequent(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            # delete node
            self.deleteNodeFromLinkedList(node)
            # move node to most recent
            self.moveToFrequent(node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node
            # move node(new) to most recent
            self.moveToFrequent(node)
            if len(self.cache) > self.capacity:
                #delete the least recently used node
                temp = self.start.next
                self.deleteNodeFromLinkedList(temp)
                #delete it from cache
                del self.cache[temp.key]

    def deleteNodeFromLinkedList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def moveToFrequent(self, node):
        temp = self.end.prev
        temp.next = node
        node.prev = temp
        self.end.prev = node
        node.next = self.end

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)