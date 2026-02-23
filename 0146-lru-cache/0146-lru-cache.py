class ListNode:
    def __init__(self):
        self.val = None
        self.key = None
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> node
        self.start = ListNode() #least recently used
        self.end = ListNode() #newest
        self.start.next = self.end
        self.end.prev = self.start

    def move_to_end(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        self.put_to_the_end(node)
    
    def put_to_the_end(self, node):
        temp = self.end.prev
        temp.next = node
        self.end.prev = node
        node.prev = temp
        node.next = self.end
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_end(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_to_end(node)
        else:
            node = ListNode()
            node.val = value
            node.key = key
            self.cache[key] = node
            self.put_to_the_end(node)

            if len(self.cache) > self.capacity:
                temp_remove = self.start.next
                temp_key = temp_remove.key
                del self.cache[temp_key]
                self.start.next = temp_remove.next
                temp_remove.next.prev = self.start 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)













