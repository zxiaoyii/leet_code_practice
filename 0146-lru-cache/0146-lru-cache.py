class ListNode:
    def __init__(self, key = 0, val = 0):
        self.prev = None
        self.next = None
        self.key = key 
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.start = ListNode() # less recently used
        self.end = ListNode() # most recently used
        self.start.next = self.end
        self.end.prev = self.start
        self.cache = {} # store key - node pairs

    def movetofq(self, node):
        a = node.next
        b = node.prev
        if a and b:
            a.prev = b
            b.next = a
            node.next = None
            node.prev = None
        c = self.end.prev 
        c.next = node
        node.prev = c
        self.end.prev = node
        node.next = self.end 

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # move node to most frequent
            self.movetofq(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            # Move node to most frequent
            self.movetofq(node)
            # update cache
            # update val
            node.val = value
            self.cache[key] = node
        else:
            # check capacity
            if len(self.cache) == self.capacity:
                # delete lru
                temp = self.start.next
                del self.cache[temp.key]
                self.start.next = temp.next
                temp.next.prev = self.start
            # new node 
            node = ListNode(key, value)
            # new node to most frequent
            self.movetofq(node)
            # new node to cache
            self.cache[key] = node
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)