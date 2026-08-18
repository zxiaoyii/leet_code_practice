class ListNode:
    def __init__(self, count = 0):
        self.keys = set()
        self.count = count
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.start = ListNode()
        self.end = ListNode()
        self.start.next = self.end
        self.end.prev = self.start
        self.cache = {} #key -> node

    def inc(self, key: str) -> None:
        if key in self.cache:
            node = self.cache[key]
            c = node.count
            node.keys.discard(key)
            
            if node.next.count == c + 1:
                node.next.keys.add(key)
                self.cache[key] = node.next
            else:
                new = ListNode(c + 1)
                n = node.next
                node.next = new 
                new.next = n
                n.prev = new
                new.prev = node
                new.keys.add(key)
                self.cache[key] = new
            if len(node.keys) == 0:
                p = node.prev
                n = node.next
                p.next = n
                n.prev = p
        else:
            node = self.start.next
            if node.count == 1:
                node.keys.add(key)
                self.cache[key] = node
            else:
                new = ListNode(1)
                new.keys.add(key)
                self.start.next = new
                new.next = node
                node.prev = new
                new.prev = self.start
                self.cache[key] = new

    def dec(self, key: str) -> None:
        node = self.cache[key]
        count = node.count
        node.keys.discard(key)
       
        if count == 1:
            del self.cache[key]
        else:
            if node.prev.count == count - 1:
                node.prev.keys.add(key)
                self.cache[key] = node.prev
            else:
                new = ListNode(node.count - 1)
                p = node.prev
                node.prev = new 
                new.prev = p
                p.next = new
                new.next = node
                new.keys.add(key)
                self.cache[key] = new
        if len(node.keys) == 0:
            p = node.prev
            n = node.next
            p.next = n
            n.prev = p
    def getMaxKey(self) -> str:
        if self.end.prev == self.start:
            return ""
        return next(iter(self.end.prev.keys))
        
    def getMinKey(self) -> str:
        if self.start.next == self.end:
            return ""
        return next(iter(self.start.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()